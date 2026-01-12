from rich.console import Console 
from rich.theme import Theme
my_theme = Theme({'markdown.code':'cyan', 'markdown.item.number':'yellow'})
console = Console(highlight=False, soft_wrap=False, theme=my_theme)