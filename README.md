# Titan Network - Bot Otomasi Airdrop

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

## 📊 Monitoring
Program akan menampilkan:
- Total nodes yang aktif
- Total earnings yang didapat
- Status koneksi real-time
- Error log jika ada

## 🔄 Update
Untuk update terbaru:
```bash
git pull origin main
```

## 📞 Kontak
- GitHub Issues: [Buat issue baru](https://github.com/username/titan-network/issues)
- Email: support@titan-network.com

## ⚠️ Disclaimer
Gunakan dengan bijak dan sesuai dengan terms of service platform target. Kami tidak bertanggung jawab atas penggunaan yang melanggar ketentuan platform.

---
**Titan Network - Your Gateway to Automated Airdrop Success!**
