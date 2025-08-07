#!/usr/bin/env python3
"""
QuantumFlow Node Automation System
A next-generation decentralized network automation framework
Author: Quantum Development Team
Version: 1.0.0-RC1
"""

import asyncio
import aiohttp
import json
import uuid
import time
import os
import sys
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
import logging
from dataclasses import dataclass, asdict
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Colorful banner
BANNER = """
\033[95m████████╗██╗████████╗ █████╗ ███╗   ██╗    ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗\033[0m
\033[94m╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗  ██║    ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝\033[0m
\033[93m   ██║   ██║   ██║   ███████║██╔██╗ ██║    ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ \033[0m
\033[92m   ██║   ██║   ██║   ██╔══██║██║╚██╗██║    ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗ \033[0m
\033[91m   ██║   ██║   ██║   ██║  ██║██║ ╚████║    ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗\033[0m
\033[96m   ╚═╝   ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝\033[0m
\033[97m                    Airdrop Independen v1.0.0\033[0m
"""

@dataclass
class NodeConfig:
    """Configuration structure for node operations"""
    api_endpoint: str = "https://api.quantumnet.dev/v2"
    ws_endpoint: str = "wss://ws.quantumnet.dev/v2/stream"
    node_version: str = "1.0.0-RC1"
    language: str = "en-US"
    retry_attempts: int = 3
    timeout_seconds: int = 30

@dataclass
class AccountCredentials:
    """Account authentication structure"""
    email: str
    password: str
    device_id: str
    session_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_at: Optional[int] = None

class QuantumNodeOrchestrator:
    """Main orchestrator for quantum node operations"""
    
    def __init__(self) -> None:
        self.config = NodeConfig()
        self.accounts: Dict[str, AccountCredentials] = {}
        self.active_sessions: Dict[str, aiohttp.ClientSession] = {}
        self.proxy_pool: List[str] = []
        self.stats = {
            'total_nodes': 0,
            'active_connections': 0,
            'total_earnings': 0.0,
            'uptime_start': datetime.now(timezone.utc)
        }
        
    def display_banner(self):
        """Display colorful startup banner"""
        print(BANNER)
        
    def generate_device_fingerprint(self) -> str:
        """Generate unique device identifier"""
        return str(uuid.uuid4())
    
    def load_configuration(self) -> Dict[str, Any]:
        """Load configuration from files"""
        config_files = ['accounts.json', 'proxies.txt', 'settings.json']
        loaded_data = {}
        
        for file in config_files:
            file_path = Path(file)
            if file_path.exists():
                if file.endswith('.json'):
                    with open(file_path, 'r') as f:
                        loaded_data[file] = json.load(f)
                else:
                    with open(file_path, 'r') as f:
                        loaded_data[file] = [line.strip() for line in f if line.strip()]
        
        return loaded_data
    
    async def initialize_proxy_pool(self, proxy_source: str = 'auto') -> None:
        """Initialize proxy pool from various sources"""
        if proxy_source == 'auto':
            # Fetch from multiple sources
            sources = [
                "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt"
            ]
            
            for source in sources:
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(source, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                            if resp.status == 200:
                                content = await resp.text()
                                self.proxy_pool.extend([f"http://{p}" for p in content.splitlines() if p.strip()])
                except:
                    continue
        
        elif Path('proxies.txt').exists():
            with open('proxies.txt', 'r') as f:
                self.proxy_pool = [line.strip() for line in f if line.strip()]
    
    def get_next_proxy(self) -> Optional[str]:
        """Get next proxy from pool with rotation"""
        if not self.proxy_pool:
            return None
        
        proxy = self.proxy_pool.pop(0)
        self.proxy_pool.append(proxy)
        return proxy
    
    async def authenticate_account(self, credentials: AccountCredentials, proxy: Optional[str] = None) -> bool:
        """Authenticate account and establish session"""
        auth_data = {
            "identifier": credentials.email,
            "secret": credentials.password,
            "device_id": credentials.device_id
        }
        
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'QuantumNode/1.0.0',
            'Accept': 'application/json'
        }
        
        connector = None
        if proxy and proxy.startswith('socks'):
            from aiohttp_socks import ProxyConnector
            connector = ProxyConnector.from_url(proxy)
        
        async with aiohttp.ClientSession(
            connector=connector,
            timeout=aiohttp.ClientTimeout(total=self.config.timeout_seconds)
        ) as session:
            
            try:
                async with session.post(
                    f"{self.config.api_endpoint}/auth/login",
                    json=auth_data,
                    headers=headers,
                    proxy=proxy if proxy and not proxy.startswith('socks') else None
                ) as response:
                    
                    if response.status == 200:
                        result = await response.json()
                        credentials.session_token = result.get('access_token')
                        credentials.refresh_token = result.get('refresh_token')
                        credentials.expires_at = int(time.time()) + result.get('expires_in', 3600)
                        self.accounts[credentials.email] = credentials
                        return True
                        
            except Exception as e:
                logger.error(f"Authentication failed for {credentials.email}: {e}")
        
        return False
    
    async def register_node(self, credentials: AccountCredentials, proxy: Optional[str] = None) -> bool:
        """Register node with the network"""
        if not credentials.session_token:
            return False
        
        node_data = {
            "device_id": credentials.device_id,
            "node_version": self.config.node_version,
            "capabilities": ["mining", "validation", "storage"],
            "location": "auto-detect"
        }
        
        headers = {
            'Authorization': f'Bearer {credentials.session_token}',
            'Content-Type': 'application/json'
        }
        
        connector = None
        if proxy and proxy.startswith('socks'):
            from aiohttp_socks import ProxyConnector
            connector = ProxyConnector.from_url(proxy)
        
        async with aiohttp.ClientSession(
            connector=connector,
            timeout=aiohttp.ClientTimeout(total=self.config.timeout_seconds)
        ) as session:
            
            try:
                async with session.post(
                    f"{self.config.api_endpoint}/nodes/register",
                    json=node_data,
                    headers=headers,
                    proxy=proxy if proxy and not proxy.startswith('socks') else None
                ) as response:
                    
                    return response.status == 201
                    
            except Exception as e:
                logger.error(f"Node registration failed: {e}")
        
        return False
    
    async def establish_websocket_connection(self, credentials: AccountCredentials, proxy: Optional[str] = None) -> None:
        """Establish WebSocket connection for real-time updates"""
        ws_url = f"{self.config.ws_endpoint}?token={credentials.session_token}&device={credentials.device_id}"
        
        connector = None
        if proxy and proxy.startswith('socks'):
            from aiohttp_socks import ProxyConnector
            connector = ProxyConnector.from_url(proxy)
        
        async with aiohttp.ClientSession(
            connector=connector,
            timeout=aiohttp.ClientTimeout(total=300)
        ) as session:
            
            try:
                async with session.ws_connect(
                    ws_url,
                    proxy=proxy if proxy and not proxy.startswith('socks') else None
                ) as ws:
                    
                    logger.info(f"WebSocket connected for {credentials.email}")
                    
                    async for msg in ws:
                        if msg.type == aiohttp.WSMsgType.TEXT:
                            data = json.loads(msg.data)
                            
                            if data.get('type') == 'reward':
                                amount = data.get('amount', 0)
                                self.stats['total_earnings'] += amount
                                logger.info(f"Reward received: {amount} tokens")
                            
                        elif msg.type == aiohttp.WSMsgType.ERROR:
                            break
                            
            except Exception as e:
                logger.error(f"WebSocket error for {credentials.email}: {e}")
    
    async def refresh_session_token(self, credentials: AccountCredentials, proxy: Optional[str] = None) -> bool:
        """Refresh authentication token"""
        if not credentials.refresh_token:
            return False
        
        refresh_data = {
            "refresh_token": credentials.refresh_token,
            "device_id": credentials.device_id
        }
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.config.timeout_seconds)
        ) as session:
            
            try:
                async with session.post(
                    f"{self.config.api_endpoint}/auth/refresh",
                    json=refresh_data,
                    headers=headers,
                    proxy=proxy if proxy and not proxy.startswith('socks') else None
                ) as response:
                    
                    if response.status == 200:
                        result = await response.json()
                        credentials.session_token = result.get('access_token')
                        credentials.expires_at = int(time.time()) + result.get('expires_in', 3600)
                        return True
                        
            except Exception as e:
                logger.error(f"Token refresh failed: {e}")
        
        return False
    
    async def process_single_account(self, email: str, password: str, use_proxy: bool, rotate_proxy: bool) -> None:
        """Process a single account through all stages"""
        device_id = self.generate_device_fingerprint()
        credentials = AccountCredentials(email=email, password=password, device_id=device_id)
        
        proxy = self.get_next_proxy() if use_proxy else None
        
        # Authenticate
        if not await self.authenticate_account(credentials, proxy):
            logger.error(f"Failed to authenticate {email}")
            return
        
        # Register node
        if not await self.register_node(credentials, proxy):
            logger.error(f"Failed to register node for {email}")
            return
        
        # Start WebSocket connection
        await self.establish_websocket_connection(credentials, proxy)
    
    async def run_orchestrator(self) -> None:
        """Main orchestrator execution"""
        self.display_banner()
        logger.info("Memulai Quantum Node Orchestrator...")
        
        # Load configuration
        config_data = self.load_configuration()
        
        # Initialize proxy pool
        await self.initialize_proxy_pool()
        
        # Load accounts
        accounts = config_data.get('accounts.json', [])
        if not accounts:
            logger.error("Tidak ada akun yang ditemukan di accounts.json")
            return
        
        # Process each account
        tasks = []
        for account in accounts:
            if account:
                email = account.get("Email")
                refresh_token = account.get("RefreshToken")
                
                if email and refresh_token:
                    user_agent = "QuantumNode/1.0.0"
                    
                    self.accounts[email] = AccountCredentials(
                        email=email,
                        password="",  # Password is not used when refresh token is provided
                        device_id=self.generate_device_fingerprint(),
                        refresh_token=refresh_token
                    )
                    
                    tasks.append(asyncio.create_task(self.process_single_account_with_refresh_token(
                        email, refresh_token,
                        use_proxy=len(self.proxy_pool) > 0,
                        rotate_proxy=True
                    )))
        
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        bot = QuantumNodeOrchestrator()
        asyncio.run(bot.run_orchestrator())
    except KeyboardInterrupt:
        logger.info("Shutting down gracefully...")
