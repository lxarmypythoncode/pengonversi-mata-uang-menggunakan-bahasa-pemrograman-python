def convert_currency(amount, rate):
    return amount * rate

def main():
    print("Pengonversi Mata Uang")
    amount = float(input("Masukkan jumlah uang: "))
    from_currency = input("Dari mata uang (misal: USD): ")
    to_currency = input("Ke mata uang (misal: IDR): ")
    
    # Contoh nilai tukar tetap
    exchange_rates = {
        "USDIDR": 15000,
        "IDRUSD": 0.000067
    }

    rate_key = from_currency + to_currency
    if rate_key in exchange_rates:
        converted = convert_currency(amount, exchange_rates[rate_key])
        print(f"{amount} {from_currency} = {converted} {to_currency}")
    else:
        print("Kurs tidak ditemukan.")

if __name__ == "__main__":
    main()
