import typer
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from bot.orders import place_order

app = typer.Typer(help="Elite Binance Futures Testnet Trading Bot")
console = Console()

@app.command()
def trade(
    symbol: str = typer.Argument(..., help="Trading pair, e.g., BTCUSDT"),
    side: str = typer.Argument(..., help="BUY or SELL"),
    order_type: str = typer.Argument(..., help="MARKET, LIMIT, or STOP_MARKET"),
    quantity: float = typer.Argument(..., help="Amount to trade"),
    price: float = typer.Option(None, "--price", "-p", help="Required for LIMIT orders"),
    stop_price: float = typer.Option(None, "--stop-price", "-s", help="Required for STOP_MARKET orders")
):
    """
    Execute a trade on Binance Futures Testnet.
    """
    console.print("\n[bold cyan]Initiating Order Request...[/bold cyan]")
    
    try:
        response = place_order(symbol, side, order_type, quantity, price, stop_price)
        
        # Displaying a clean table for order response
        table = Table(title="Order Execution Summary", show_header=True, header_style="bold green")
        table.add_column("Order ID", style="dim")
        table.add_column("Symbol")
        table.add_column("Side")
        table.add_column("Type")
        table.add_column("Status")
        table.add_column("Executed Qty")
        
        table.add_row(
            str(response.get('orderId')),
            response.get('symbol'),
            response.get('side'),
            response.get('origType'),
            response.get('status'),
            str(response.get('executedQty'))
        )
        
        console.print(table)
        console.print("[bold green]✔ Order successfully placed![/bold green]\n")
        
    except Exception as e:
        console.print(f"[bold red]✘ Order Failed:[/bold red] {e}\n")

if __name__ == "__main__":
    app()