# Avtomobil Inventar Tizimi - Tahrirlash Funksiyasi Hujjatlari

## Umumiy ma'lumot
Python va Tkinter yordamida avtomobil inventar tizimini tahrirlash funksiyasini amalga oshirish bo'yicha qo'llanma.

## Amalga oshirish bosqichlari

### 1-bosqich: Tahrirlash oynasi funksiyasi
```python
# Tanlangan avtomobilni tahrirlash funksiyasi
def edit_car(tree):
   # Treeview dan tanlangan elementni olish
   selected_item = tree.selection()
   # Agar avtomobil tanlanmagan bo'lsa xatolik xabari
   if not selected_item:
       messagebox.showerror("Xato", "Iltimos, tahrirlash uchun avtomobilni tanlang")
       return
   # Tanlangan avtomobil ma'lumotlarini olish
   car_values = tree.item(selected_item)['values']

    # Yangi oyna yaratish
    window = tk.Toplevel()
    window.title("Avtomobilni tahrirlash")
    window.geometry("300x250")

    # Markasi uchun maydon
    ttk.Label(window, text="Markasi: ").grid(row=0, column=0, padx=5, pady=5)
    make_input = ttk.Entry(window)
    # Joriy qiymat bilan to'ldirish
    make_input.insert(0, car_values[1])
    make_input.grid(row=0, column=1)

    def save_changes():
        # Maydonlardan yangi qiymatlarni olish
        make = make_input.get()
        model = model_input.get()
        year = year_input.get()
        price = price_input.get()

        # Maydonlar to'ldirilganini tekshirish
        if not all([make, model, year, price]):
            messagebox.showerror("Xato", "Barcha maydonlarni to'ldiring")
            return
```

## Main windowda
```python

    # Asosiy oynaga tahrirlash tugmasini qo'shish
    ttk.Button(crud_frame, command=lambda: edit_car(tree), 
           text="Tanlangan avtomobilni tahrirlash").grid(
        row=1, column=0, pady=10, padx=5, sticky="ew"
    )
```