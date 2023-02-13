''' Bellmanning funksional tenglamasini ishlash uchun GUI dastur. '''
'''
Ushbu dastur python dasturlash tilida ishlab chiqildi. Dastur ishlashi uchun
ba'zi komponentalar zarur bo'ladi. 
    1: assets/ ushbu katalogda rasmlar mavjud. Agarda ushbu katalogdagi rasmlar bo'lmasa yoki 
        katalogning o'zi mavjud bo'lmasa dastur kutilganidek ishlamaydi. Bular juda muhim.
    2: 'utils' funksiyalar kutubxonasi. Ushbu kutubxonada Task, Solution, IterableList sinflari 
        mavjud. Ushbu sinflar misolning ishlanishiga javobgardir. Ular bo'lmasa dastur hisob kitob
        ishlarini amalga oshira olmaydi. Ushbu sinflarni o'zim yozib chiqqanman. Boshqa joydan yuklab 
        olib bo'lmaydi. Diqqat, agar ushbu sinfar mavjud bo'lmasa GUI ishga tushishi mumkin, ammo hisob kitobda 
        dastur xatolik beradi.
    3: 'pillow' kutubxonasi rasmlarni yuklab olish uchun ishlatildi. "from PIL import ImageTk, Image".
        Dasturni ishlatishdan oldin ushbu kutubxona mavjudligini tekshirib oling. Buni bilish uchun cmd dasturini ochib 
        "pip freeze" buyrug'i yoziladi. Agar chiqqan ma'lumotlar ichida 'pillow' bo'lmasa demak u o'rnatilmagan.
        "pillow" kutubxonasini yuklab olish quyidagicha: cmd dasturini ishga tushiramiz va quyidagi buyruqni kiritamiz.
        "pip install pillow". Agar sizda pip buyrug'i ishlamasa ushbu havola orqali o'tib uni qanday o'rnatish mumkinligini bilib olasiz.
        https://www.dataquest.io/blog/installing-python-on-windows/#:~:text=To%20do%20so%2C%20open%20the,and%20type%20there%20python%20%2DV%20.

        
Barcha komponentalar to'liq mavjud bo'lsa dasturni ishga tushiramiz. Bunda dastur 'main.py' fayli bilan ishga tushiriladi. Ya'ni
aynan mana shu fayl dasturning boshlanish qismi hisoblanadi. cmd dasturini ishga tushirib ushbu 'main.py' faylining
yoniga kelamiz. Va ushbu buyruqni kiritamiz. "python main.py". 

# ################ 
DIQQAT !!!!!!!
Ushbu dastur windows 10 operatsion tizimida ishlab chiqildi. Boshqa OSlarda xatolik berishi ehtimoldan holi emas.

Dasturchi: 
    familya/ism: Oromov Akobir
    email: cpp.coder.uz.oa@gmail.com
    github: https://github.com/CppCoderUz

Dastur:
    versiya: 1.0.0
    dasturlash tili: python
    nomi: Bellman funksional tenglamasi
    sertifikat: Yo'q
    holati: Aktiv, barcha uchun ochiq 

'''

import tkinter as tk
from PIL import ImageTk, Image
from utils import Task, Solution


images = [
    Image.open('assets/f_1.png').resize(size=(100, 30)),
    Image.open('assets/f_2.png').resize(size=(100, 30)),
    Image.open('assets/f_3.png').resize(size=(100, 30)),
    Image.open('assets/f_4.png').resize(size=(100, 30)),
    Image.open('assets/f_5.png').resize(size=(100, 30)),
]

index_x = [
    Image.open('assets/x_1.png').resize(size=(35, 30)),
    Image.open('assets/x_2.png').resize(size=(35, 30)),
    Image.open('assets/x_3.png').resize(size=(35, 30)),
    Image.open('assets/x_4.png').resize(size=(35, 30)),
    Image.open('assets/x_5.png').resize(size=(35, 30)),
]


class MaxFunction:
    def __init__(self, *arg, **kwargs):
        self.n = 5
        self.task_list = [True, True, True, True, True]
        self.index_list = [True, True, True, True, True]
        self.window = tk.Tk()
        self.img = [True, True, True, True, True]
        self.img[0] = ImageTk.PhotoImage(image=images[0])
        self.img[1] = ImageTk.PhotoImage(image=images[1])
        self.img[2] = ImageTk.PhotoImage(image=images[2])
        self.img[3] = ImageTk.PhotoImage(image=images[3])
        self.img[4] = ImageTk.PhotoImage(image=images[4])
        
        self.picture_x = [True, True, True, True, True]
        self.picture_x[0] = ImageTk.PhotoImage(image=index_x[0])
        self.picture_x[1] = ImageTk.PhotoImage(image=index_x[1])
        self.picture_x[2] = ImageTk.PhotoImage(image=index_x[2])
        self.picture_x[3] = ImageTk.PhotoImage(image=index_x[3])
        self.picture_x[4] = ImageTk.PhotoImage(image=index_x[4])

        self.button_f = [True, True, True, True, True]
        self.button_f[0] = tk.Button(self.window, image=self.img[0], state=tk.DISABLED)
        self.button_f[0].place(x=10, y=100)

        self.button_f[1] = tk.Button(self.window, image=self.img[1], state=tk.DISABLED)
        self.button_f[1].place(x=10, y=160)
        
        self.button_f[2] = tk.Button(self.window, image=self.img[2], state=tk.DISABLED)
        self.button_f[2].place(x=10, y=220)
        
        self.button_f[3] = tk.Button(self.window, image=self.img[3], state=tk.DISABLED)
        self.button_f[3].place(x=10, y=280)
        
        self.button_f[4] = tk.Button(self.window, image=self.img[4], state=tk.DISABLED)
        self.button_f[4].place(x=10, y=340)


        self.task_list[0] = tk.Entry(self.window, textvariable=1, font=('Arial 15'))
        self.task_list[0].place(height=30, width=350, x=120, y=100)

        self.task_list[1] = tk.Entry(self.window, textvariable=2, font=('Arial 15'))
        self.task_list[1].place(height=30, width=350, x=120, y=160)

        self.task_list[2] = tk.Entry(self.window, textvariable=3, font=('Arial 15'))
        self.task_list[2].place(height=30, width=350, x=120, y=220)

        self.task_list[3] = tk.Entry(self.window, textvariable=4, font=('Arial 15'))
        self.task_list[3].place(height=30, width=350, x=120, y=280)

        self.task_list[4] = tk.Entry(self.window, textvariable=5, font=('Arial 15'))
        self.task_list[4].place(height=30, width=350, x=120, y=340)

        self.index_list[0] = tk.Entry(self.window, textvariable=6, font=('Arial 15'))  
        self.index_list[0].place(height=30, width=40, x=500, y=100)       

        self.index_list[1] = tk.Entry(self.window, textvariable=7, font=('Arial 15'))  
        self.index_list[1].place(height=30, width=40, x=550, y=100)

        self.index_list[2] = tk.Entry(self.window, textvariable=8, font=('Arial 15'))  
        self.index_list[2].place(height=30, width=40, x=600, y=100)

        self.index_list[3] = tk.Entry(self.window, textvariable=9, font=('Arial 15'))  
        self.index_list[3].place(height=30, width=40, x=650, y=100)

        self.index_list[4] = tk.Entry(self.window, textvariable=10, font=('Arial 15'))  
        self.index_list[4].place(height=30, width=40, x=700, y=100)  
        
        self.b = tk.Entry(self.window, textvariable=11, font=('Arial 15'))
        self.b.place(height=30, width=40, x=800, y=100)

        self.button_equal = tk.Button(self.window, text='=', command=self.click_equal, font=('Arial 15'))
        self.button_equal.place(width=40, height=30, x=750, y=100)

        self.index_list_x = [True, True, True, True, True]
        
        self.index_list_x[0] = tk.Button(self.window, image=self.picture_x[0], state=tk.DISABLED)
        self.index_list_x[0].place(x=500, y=50)

        self.index_list_x[1] = tk.Button(self.window, image=self.picture_x[1], state=tk.DISABLED)
        self.index_list_x[1].place(x=550, y=50)

        self.index_list_x[2] = tk.Button(self.window, image=self.picture_x[2], state=tk.DISABLED)
        self.index_list_x[2].place(x=600, y=50)

        self.index_list_x[3] = tk.Button(self.window, image=self.picture_x[3], state=tk.DISABLED)
        self.index_list_x[3].place(x=650, y=50)

        self.index_list_x[4] = tk.Button(self.window, image=self.picture_x[4], state=tk.DISABLED)
        self.index_list_x[4].place(x=700, y=50)

        self.b_button = tk.Button(self.window, text='b', state=tk.DISABLED, font=('Arial 15'))
        self.b_button.place(x=800, y=50, width=40, height=35)
        
        self.button_hisoblash = tk.Button(self.window, text='Hisoblash', font=('Arial 15'), command=self.hisoblash)
        self.button_hisoblash.place(x = 10, y=500, width=490, height=30)

        self.natija_max = tk.Button(self.window, text='Natija', font=('Arial 15'), state=tk.DISABLED)
        self.natija_max.place(x=500, y=150, width=350, height=30)

        # Maksimal yechimlar
        self.max = tk.Button(self.window, text='max', font=('Arial 15'), state=tk.DISABLED)
        self.max.place(x=500, y=200, width=50, height=30)
        # Maksimal yechim qiymati chiquvchi oyna
        self.max_value = tk.Button(self.window, text='0', font=('Arial 15'), state=tk.DISABLED)
        self.max_value.place(x=550, y=200, width=300, height=30)
        # Maksimal qiymat chiquvchi oyna yechimlari
        self.max_value_indexs = tk.Button(self.window, text='', font=('Arial 15'), state=tk.DISABLED)
        self.max_value_indexs.place(x=500, y=230, width=350, height=30)


        # Minimal yechimlar
        self.min = tk.Button(self.window, text='min', font=('Arial 15'), state=tk.DISABLED)
        self.min.place(x=500, y=300, width=50, height=30)
        # Minimal yechim qiymati chiquvchi oyna
        self.min_value = tk.Button(self.window, text='0', font=('Arial 15'), state=tk.DISABLED)
        self.min_value.place(x=550, y=300, width=300, height=30)
        # Minimal qiymat chiquvchi oyna yechimlari
        self.min_value_indexs = tk.Button(self.window, text='', font=('Arial 15'), state=tk.DISABLED)
        self.min_value_indexs.place(x=500, y=330, width=350, height=30)

        self.error_log = tk.Button(self.window, text='', state=tk.DISABLED, font=('Arial 15'))
        self.error_log.place(x=500, y=400, width=350, height=50)

        self.draw()
        

    def draw(self):
        self.window.title('Bellmanning funksional tenglamasi')
        self.window.geometry('900x600+100+100')
        
        tk.Button(self.window, text='Funksiyalar sonini kiriting:', 
            width='67', height='2', state=tk.DISABLED, 
        ).place(x=0,y=0)

        tk.Button(self.window, text='Indekslarni kiriting :', 
            width='50', height='2', state=tk.DISABLED, 
        ).place(x=500,y=0)


        self.button_n = tk.Button(self.window, text=str(self.n), padx=15, width=10,
            font=tk.BOTH, state='disabled'
        )
        self.button_n.place(x=150, y=45)

        self.button_plyus = tk.Button(self.window, text=' + ', width=4, height=2,
            command=self.click_plyus
        )
        self.button_plyus.place(x=110, y=45)

        self.button_minus = tk.Button(self.window, text=' - ', width=4, height=2,
            command=self.click_minus
        )
        self.button_minus.place(x=300, y=45)

        self.window.mainloop()

    def click_minus(self):
        if not self.n == 1:
            self.button_f[self.n-1].place(x=0,y=0)
            self.index_list[self.n-1].place(x=0,y=0)
            self.index_list_x[self.n-1].place(x=0, y=0)
            self.task_list[self.n-1].place(x=0, y=0)
            self.n -= 1
            self.button_plyus.configure(state=tk.ACTIVE)
        else:
            self.button_minus.configure(state=tk.DISABLED)

        self.button_n.config(text='%s'%self.n)
    
    def click_plyus(self):
        self.n += 1
        if not self.n == 6:
            self.button_f[self.n - 1].place(x=10, y=40 + self.n*60)
            self.task_list[self.n -1].place(x=120, y=40 + self.n*60)
            self.index_list[self.n-1].place(x=self.n * 50 + 450, y=100)
            self.index_list_x[self.n-1].place(x=self.n*50 + 450, y=50)
            
            self.button_minus.configure(state=tk.ACTIVE)
        else:
            self.n -= 1
            self.button_f[4].place(x=10, y=340)
            self.task_list[4].place(x=120, y=340)
            self.index_list[4].place(x=700, y=100)
            self.button_plyus.configure(state=tk.DISABLED)

        self.button_n.config(text='%s'%self.n)

    def click_equal(self):
        if self.button_equal['text'] == '=':
            self.button_equal['text'] = '<='
        elif self.button_equal['text'] == '<=':
            self.button_equal['text'] = '='
        else:
            print("Error")
    
    def hisoblash(self):
        tasks = []
        counter = 0
        for i in self.task_list[:self.n]:
            counter += 1
            if not Task(i.get()).is_right():
                self.error_clear(error='%s-funksiyada xatolik'%str(counter), _none=False)
                return
            tasks.append(i.get())
        
        counter = 0
        indexs = []
        for i in self.index_list[:self.n]:
            counter += 1
            try:
                int(i.get())
            except:
                self.error_clear(error='%s-indeksda xatolik'%str(counter), _none=False)
                return
            indexs.append(int(i.get()))
        b = str()
        try:
            b = int(self.b.get())
        except:
            self.error_clear(error='b-ni kiriting', _none=False)
            return
        
        character = self.button_equal['text']
        if character == '=':
            character = False
        else:
            character = True
        solve = Solution(b=b, index_list=indexs, n=self.n, task_list=tasks, shart=character)._solve()
        
        if not solve['rezault']:
            self.error_clear(error=solve['message'], _none=True)
            return

        self.min_value['text'] = solve['min']['value']
        self.min_value_indexs['text'] = ', '.join(map(str, solve['min']['list']))

        self.max_value['text'] = solve['max']['value']
        self.max_value_indexs['text'] = ', '.join(map(str, solve['max']['list']))

        self.error_log['text'] = ''
    
    def error_clear(self, error:str, _none = False):
        self.error_log['text'] = error
        if _none:
            self.min_value['text'] = ''
            self.min_value_indexs['text'] = ''
            self.max_value['text'] = ''
            self.max_value_indexs['text'] = ''




MaxFunction()
