# Elite Binance Futures Testnet Trading Bot (USDT-M)

A production-ready, modular Python CLI application built to execute trades programmatically on the Binance Futures Testnet platform using secure asynchronous API interactions.

## 🚀 Key Features Built From Scratch
- **Modular Architecture:** Clean segregation between the configuration layers, core API wrappers, structural validation, and interactive CLI layout.
- **Advanced CLI UX:** Leverages `Typer` and `Rich` to handle input arguments gracefully and output beautiful, scannable execution tables natively in the terminal.
- **Robust Exception Handling:** Full validation patterns to intercept bad user inputs locally before exhausting API limits or facing server-side connection errors.
- **Comprehensive Activity Logging:** Automated structural tracing that captures timestamps, operational payloads, and network receipts inside a dedicated file handler.
- **Bonus Implementation:** Built support for an optional third conditional order type (`STOP_MARKET`) along with enhanced CLI interface styling.

---

## 🛠️ Local System Configuration

### 1. Prerequisites
Ensure your local environment has Python 3.8+ installed on your system.

### 2. Virtual Environment Setup
Isolate package dependencies cleanly inside your project space:
```bash
# Initialize the workspace environment
python3 -m venv venv

# Activate on MacOS/Linux:
source venv/bin/activate

# Activate on Windows:
.\venv\Scripts\activate

3. Dependency Installation
Install verified package sets cleanly via the lock-file tracking rules:
Bash
pip install -r requirements.txt
4. Credentials Setup
Create a file named .env in the root workspace directory and append your secure Testnet account keys (never expose these keys publicly):
Plaintext
BINANCE_API_KEY=your_actual_testnet_api_key_here
BINANCE_API_SECRET=your_actual_testnet_api_secret_here