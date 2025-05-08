import pyfiglet
import random
from pystyle import Colors, Colorate, Center, Box, Write, System
import os
import time
from typing import List, Tuple

# Constants
FONT_COUNT = 549
FONTS_PER_PAGE = 10

class PyFigletUltra:
    def __init__(self):
        self.fonts = pyfiglet.FigletFont.getFonts()
        System.Size(120, 40)
        System.Title("Rumstyle Ultra - MAXIMAL BEAUTIFUL Edition")
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_welcome(self):
        self.clear_screen()
        welcome_art = pyfiglet.figlet_format("Rumstyle Ultra", font="slant")
        print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(welcome_art)))
        
        subtitle = "MAXIMAL BEAUTIFUL Edition".center(120)
        print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(subtitle)))
        
        credit = "Created by rum • @Rumyp".center(120)
        print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(credit)))
        
        print("\n"*2)
        
    def draw_menu_box(self, options: List[str]) -> str:
        menu_content = "\n".join([f"{i+1}. {option}" for i, option in enumerate(options)])
        return Box.DoubleCube(menu_content)
        
    def get_user_input(self) -> Tuple[str, int]:
        print(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter("✨ CREATE YOUR MASTERPIECE ✨")))
        print("\n")
        
        text = Write.Input("Enter your text -> ", Colors.cyan_to_green, interval=0.05)
        print("\n")
        
        while True:
            style_num = Write.Input(f"Enter style number (1-{FONT_COUNT}) -> ", Colors.purple_to_blue, interval=0.05)
            try:
                style_num = int(style_num)
                if 1 <= style_num <= FONT_COUNT:
                    return text, style_num
                Write.Print(f"Please enter a number between 1 and {FONT_COUNT}", Colors.red_to_purple)
            except ValueError:
                Write.Print("Please enter a valid number", Colors.red_to_purple)
    
    def display_result(self, text: str, style_num: int):
        try:
            selected_font = self.fonts[style_num - 1]
            result = pyfiglet.figlet_format(text, font=selected_font)
            
            self.clear_screen()
            print(Colorate.Horizontal(Colors.rainbow, Center.XCenter("🎉 YOUR ARTWORK 🎉")))
            print("\n")
            
            colored_result = Colorate.Horizontal(random.choice([
                Colors.rainbow,
                Colors.purple_to_blue,
                Colors.cyan_to_green,
                Colors.red_to_yellow
            ]), result)
            
            print(Center.XCenter(colored_result))
            
            print("\n")
            info = f"Font: {selected_font} (Style #{style_num})"
            print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(info)))
            print("\n")
            
            Write.Input(Center.XCenter("Press ENTER to continue..."), Colors.cyan_to_green, interval=0.05)
            
        except Exception as e:
            Write.Print(f"An error occurred: {e}", Colors.red_to_purple)
    
    def show_random_samples(self):
        self.clear_screen()
        print(Colorate.Horizontal(Colors.rainbow, Center.XCenter("🎨 FONT SHOWCASE 🎨")))
        print("\n")
        
        sample_fonts = random.sample(self.fonts, min(5, len(self.fonts)))
        
        for i, font in enumerate(sample_fonts, 1):
            font_num = self.fonts.index(font) + 1
            print(Colorate.Horizontal(
                Colors.cyan_to_green,
                Center.XCenter(f"Sample #{i} (Style #{font_num} - {font})")
            ))
            
            sample_text = pyfiglet.figlet_format("BEAUTIFUL", font=font)
            print(Colorate.Horizontal(
                random.choice([Colors.purple_to_blue, Colors.red_to_yellow]),
                Center.XCenter(sample_text)
            ))
            print("\n")
        
        Write.Input(Center.XCenter("Press ENTER to continue..."), Colors.blue_to_cyan, interval=0.05)
    
    def show_font_gallery(self):
        current_page = 0
        total_pages = (len(self.fonts) + FONTS_PER_PAGE - 1) // FONTS_PER_PAGE
        
        while True:
            self.clear_screen()
            print(Colorate.Horizontal(Colors.rainbow, Center.XCenter("📖 FONT GALLERY 📖")))
            
            page_info = f"Page {current_page + 1}/{total_pages}".center(120)
            print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(page_info)))
            print("\n")
            
            start = current_page * FONTS_PER_PAGE
            end = start + FONTS_PER_PAGE
            page_fonts = self.fonts[start:end]
            
            for i, font in enumerate(page_fonts, start + 1):
                font_entry = f"{i:3}. {font}"
                print(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(font_entry)))
            
            print("\n")
            options = [
                " • n - Next page\n",
                "p - Previous page\n",
                "q - Return to main menu\n",
                "Enter number to preview"
            ]
            print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(" • ".join(options))))
            
            choice = Write.Input("\n" + Center.XCenter("Your choice -> "), Colors.cyan_to_green, interval=0.05).lower()
            
            if choice == 'n' and current_page < total_pages - 1:
                current_page += 1
            elif choice == 'p' and current_page > 0:
                current_page -= 1
            elif choice == 'q':
                break
            elif choice.isdigit():
                font_num = int(choice)
                if start < font_num <= end:
                    self.preview_font(font_num)
    
    def preview_font(self, font_num: int):
        selected_font = self.fonts[font_num - 1]
        self.clear_screen()
        
        print(Colorate.Horizontal(Colors.rainbow, Center.XCenter("🔍 FONT PREVIEW 🔍")))
        print("\n")
        
        info = f"Style #{font_num} - {selected_font}"
        print(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(info)))
        print("\n")
        
        preview_text = pyfiglet.figlet_format("PYFIGLET", font=selected_font)
        print(Colorate.Horizontal(
            random.choice([Colors.rainbow, Colors.purple_to_blue]),
            Center.XCenter(preview_text)
        ))
        
        print("\n")
        Write.Input(Center.XCenter("Press ENTER to continue..."), Colors.blue_to_cyan, interval=0.05)
    
    def main_menu(self):
        while True:
            self.clear_screen()
            self.display_welcome()
            
            options = [
                "Create your masterpiece",
                "Show random font samples",
                "Browse Font Gallery",
                "Exit"
            ]
            
            print(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(self.draw_menu_box(options))))
            print("\n")
            
            choice = Write.Input(Center.XCenter("Select an option (1-4) -> "), Colors.purple_to_blue, interval=0.05)
            
            if choice == '1':
                text, style_num = self.get_user_input()
                self.display_result(text, style_num)
            elif choice == '2':
                self.show_random_samples()
            elif choice == '3':
                self.show_font_gallery()
            elif choice == '4':
                self.exit_program()
                break
            else:
                Write.Print(Center.XCenter("Invalid choice. Please select 1-4"), Colors.red_to_purple)
                time.sleep(1)
    
    def exit_program(self):
        self.clear_screen()
        goodbye = pyfiglet.figlet_format("Goodbye!", font="slant")
        print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(goodbye)))
        
        message = "Thank you for using Rumstyle Ultra!".center(120)
        print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(message)))
        
        credit = "Created by rum • @Rumyp".center(120)
        print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(credit)))
        
        time.sleep(2)
        self.clear_screen()

if __name__ == "__main__":
    app = PyFigletUltra()
    app.main_menu()

