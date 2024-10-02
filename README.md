# pengonversi-mata-uang-menggunakan-bahasa-pemrograman-python
engonversi Mata Uang Program ini akan mengambil nilai tukar dari API atau secara manual untuk mengonversi jumlah mata uang dari satu jenis ke jenis lainnya.  Fitur: Input jumlah dan mata uang asal serta tujuan. Gunakan nilai tukar tetap atau nilai tukar dari API seperti fixer.io atau exchangeratesapi.io.


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

