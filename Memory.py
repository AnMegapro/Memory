from tkinter import *
from random import randint as rnd
import random
from tkinter import messagebox
from math import sqrt

#Здесь можно изменить рамер, нго главное чтоб он был чётным и квадраторм числа 
count=400
#Здесь можно изменить высоту блока
heightOfBlock=50
justfor="۞ ☣ ⌘ ⌗ ⋕ ※ ☬ ☫ 〄 ⎉ ⎊ ⎋ ⌑ փ۩ ☗ ☖ Ⓐ ® © ℗ ™ ⚠ � ￥ ￡ ￦ $ € ₵ ₠ ₢ ₡ ₱ ₮ ₦ ₳ ☧ ␢ ֆ ␤ ␡ ␛♲ ♳ ♴ ♵ ♶ ♷ ♸ ♹ ♺ ♻ ♼ ♽◰ ◱ ◲ ◳ ◴ ◵ ◶ ◷ ◬ ◭ ◮ ◧ ◨ ◩ ◪ ◫ ◐ ◑ ◒ ◓ ◔ ◕ ◖◗ ʘ ◈ ▣ ⌼ ⌻ ⌺ ⎄ ⎅ ⍥ ⍢ ✆ ✈ ✐ ⌨ ✑ ✒ ✂ ✉ ⎗ ⎘ ⎙ ⎚ ✔ ✓ ⎷ √ ✕ ✖ ✗ ✘ ☐ ☑ ☒ ⊕ ⊗ ⊖ ⊘ ⊙ ⊚ ⊛ ⊜ ⊝ ⊞ ⊟ ⊠ ⊡ □ ▣ ▤ ▥ ▦ ▧ ▨ ▩๑ ஐ ॐ ๖ۣۜG இ ഊ ₪₪ § Ѿ Ω Ѽ ఞ ಊ ఎ യ ⅋ ﻸ ௸ ௹ ஹ ૪ ֆ ൠ ᘘ ∫ ∬ ∭ ∮ ∯ ∰ ∱ ∲ ⇋⇌ ℵ ᕘᕚ६ ३ १ २ ५ ७ ९ ণ ঐ ঙ ৡ ১ ২ ৩ ৯ ৶ ৸ ઈ ઉ ᖗᖘ ᖙᖚ ૬ ୭ ໂ ໃ ໄ ⌇ܓ ܟ ܢ༼ ༽ Ҩ ҩ ☍☍☍ ᏜᏜᏜ ☌ ☋ ☊ ⎌⌭ ⊶⊷ ⌢ ⌣ ◜◝◞◟◠ ◡ ᴥ ܫ Ϫ ϫ ⊰⊱∴ ∵ ∶ ∷ ∸ ∹ ∺ ∻ ⁖ ⁘ ⁙ ⁚⁛ ⁜ ⁝⁞⌆ ⏀ ⏁ ⏂ ⏃ ⏄ ⏅ ⏆ ⏇ ⏈ ߐ ⎐ ⎑ ⎒ ⍙ ⍚ ⍛ ⍜ ≗ ≘ ≙ ≚ ≛ ≜ ≝ ≞ ≟√ ∫ ∂ ∑ ⅀ ∏ ☈ − ± × ÷ ≈ ∝ ⌭ ≡ ⎓ ≠ ≤ ≥ ∈ ∩ ∪ ⊂ ⊃ ⊆ ⊇ ⋋⋌ ¬ ∧ ∨ ៹៹ ៷៷ ⍱ ⍲ ⍭ ∃ ∀ ° ′ ″ ‰ ∛ ∜ √ ❛ ❜ ❝ ❞"
symbols=["☎","☀","☁","☂","☃","☻","☕","♔","★","☄","☢"]
justfor=justfor.split(" ")
symbols+=justfor
window = Tk()

window.geometry(str(int(sqrt(count)*heightOfBlock))+"x"+str(int(sqrt(count)*heightOfBlock+100)))
move=0
firstOpened=-1;
firstOpenedNum=-1;
Game=True;
def Click(event):
    global move
    global Game
    global firstOpened
    global firstOpenedNum
    
    if move%2==0:
        firstOpened=event.widget.typeP
        firstOpenedNum=event.widget.num
        
        for all in btns:
            if all.open==False:
                all["text"]=""
                
        moves["text"]="Moves:" +str(int(move/2)+1)
    btns[event.widget.num]["text"]=symbols[event.widget.typeP]
    if move%2==1 and firstOpened==event.widget.typeP and firstOpenedNum!=event.widget.num:
        btns[firstOpenedNum].config(font=("Courier", 50))
        btns[firstOpenedNum].open=True
        btns[event.widget.num].config(font=("Courier", 50))
        btns[event.widget.num].open=True
        
    move+=1
    Game=False
    for all in btns:
            if all.open==False:
                print(str(all.num)+"This")
                Game=True
    print(Game)
    if Game==False:
        name["text"]="You Won!"

   

window.bind("<Button-1>", Click)
btns=[]
pairs=list(range(0,int(count/2)))+list(range(0,int(count/2)))
random.shuffle(pairs)
for i in range(count):
    btn= Button(window, text="");
    print(pairs[i])
    btn.typeP= pairs[i]
    btn.num= i
    btn.open= False
    btns.append(btn)   
    btn.config(font=("Courier", int(heightOfBlock/4)))
    
for btn in btns:
    e=sqrt(count)
    btn.place(x=(btn.num%e)*heightOfBlock, y=(btn.num//e)*heightOfBlock+100, width=heightOfBlock,height=heightOfBlock)

name=Label(window, text="Memory")
moves=Label(window, text="Moves: 0")
name.config(font=("Courier", 40))
moves.config(font=("Courier", 20))
name.pack()
moves.place(x=10,y=10)
window.mainloop()