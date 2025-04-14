from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# 귀여운 ASCII 아트 (고양이!)
ascii_art = r"""
 /\_/\  
( o.o ) 
 > ^ <
"""

# 아트 꾸미기
title = Text("냥냥뿅!", style="bold cyan")
subtitle = Text("이건 귀여운 고양이야~ 🐱", style="italic green")

# Panel로 감싸기
console.print(Panel(ascii_art, title=title, subtitle=subtitle, border_style="bright_magenta", padding=(1, 4)))


from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# 아스카 아트 (작은 버전, 터미널 호환)
asuka_art = r"""
      ／＞　 フ
     | 　_　_| 
   ／` ミ＿xノ 
  /　　　　 |
 /　 ヽ　　 ﾉ
│　　|　|　|
／￣|　　 |　|　|
(￣ヽ＿_ヽ_)__)
＼二)
"""

# 텍스트 꾸미기
title = Text("고양이이 등장! ✨", style="bold red")
description = Text("너무 피곤하다옹옹...", style="italic magenta")

# Panel로 감싸서 출력
console.print(Panel(asuka_art, title=title, subtitle=description, border_style="red", padding=(1, 4)))
