# Titan Network Bot 

## 📋 Deskripsi
Titan Network adalah bot otomasi terbaru untuk mengikuti berbagai airdrop secara otomatis. Dirancang untuk memaksimalkan partisipasi dalam program airdrop dengan fitur multi-akun, proxy rotation, dan monitoring real-time.

## 🚀 Fitur Utama
- ✅ **Multi-Akun Support** - Kelola banyak akun sekaligus
- ✅ **Proxy Rotation** - Rotasi proxy otomatis untuk keamanan
- ✅ **Real-time Monitoring** - Pantau reward secara langsung
- ✅ **Auto Registration** - Registrasi node otomatis
- ✅ **WebSocket Connection** - Koneksi real-time untuk update terbaru

## 📦 Instalasi

### Prasyarat
- Python 3.7+
- pip (Python package manager)

### Langkah Instalasi
1. Clone repository:
   ```bash
   git clone https://github.com/username/titan-network.git
   cd titan-network
   ```

2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

3. Setup konfigurasi:
   ```bash
   # Edit file accounts.json dengan informasi akun Anda
   nano accounts.json
   ```

## ⚙️ Konfigurasi

### File accounts.json
```json
[
  {
    "Email": "email_anda@domain.com",
    "RefreshToken": "refresh_token_andi"
  },
  {
    "Email": "email_kedua@domain.com",
    "RefreshToken": "refresh_token_kedua"
  }
]
```

### File proxies.txt (Opsional)
```
http://proxy1:port
http://proxy2:port
socks5://proxy3:port
```

## 🎯 Cara Menjalankan

### Langkah 1: Persiapan
Pastikan semua file ada di folder yang sama:
- `titan.py`
- `accounts.json`
- `requirements.txt`

### Langkah 2: Install Dependensi
```bash
pip install -r requirements.txt
```

### Langkah 3: Konfigurasi Akun
Edit file `accounts.json` dengan informasi akun Anda:
```json
[
  {
    "Email": "your_email@example.com",
    "RefreshToken": "your_refresh_token_here"
  }
]
```

### Langkah 4: Jalankan Program
```bash
python titan.py
```

### Output yang Diharapkan
```
████████╗██╗████████╗ █████╗ ███╗   ██╗    ███╗   ██╗███████╗████████╗
   ██║   ██║   ██║   ███████║██╔██╗ ██║    ██╔██╗ ██║█████╗     ██║   
                    Titan Network v1.0.0
═══════════════════════════════════════════════════════════════
2025-08-07 22:20:00 | INFO | Memulai Titan Network...
2025-08-07 22:20:01 | INFO | WebSocket connected untuk email@domain.com
2025-08-07 22:20:05 | INFO | Reward received: 10 tokens
```

## 🔧 Troubleshooting

### Error: "Tidak ada akun yang ditemukan"
- Pastikan file `accounts.json` ada di root directory
- Validasi format JSON di file accounts.json

### Error: "Authentication failed"
- Periksa refresh token di accounts.json
- Pastikan email dan refresh token valid

### Error: "No module found"
- Jalankan `pip install -r requirements.txt` lagi
- Pastikan Python path sudah benar
- 
### Struktur Folder
```
titan-network/
├── titan.py          # Program utama
├── accounts.json     # Konfigurasi akun
├── requirements.txt  # Dependensi
└── README.md        # Dokumentasi GitHub
```
## 📊 Monitoring
Program akan menampilkan:
- Total nodes yang aktif
- Total earnings yang didapat
- Status koneksi real-time
- Error log jika ada


## 🌐 Komunitas & Sosial Media

Ingin berdiskusi, bertanya, atau berbagi ide? Bergabunglah dengan komunitas kami!

💬 Telegram Group: [t.me/airdropindependen](https://t.me/independendropers)

🐦 Twitter/X: [twitter.com/deasaputra12](https://x.com/Deasaputra_12)

🎮 Discord Server: [discord.gg/airdropindependen](https://discord.gg/Tuy2bR6CkU)


## Buy Me a Coffee

- **EVM:** 0x905d0505Ec007C9aDb5CF005535bfcC5E43c0B66
- **TON:** UQCFO7vVP0N8_K4JUCfqlK6tsofOF4KEhpahEEdXBMQ-MVQL
- **SOL:** BmqfjRHAKXUSKATuhbjPZfcNciN3J2DA1tqMgw9aGMdj

Thank you for visiting this repository, don't forget to contribute in the form of follows and stars.
If you have questions, find an issue, or have suggestions for improvement, feel free to contact me or open an *issue* in this GitHub repository.

**deasaputra**
