#sample server

from fastmcp import FastMCP
import random
import json

#create the mcp server instance
mcp=FastMCP("Simple calculator server")

#tool:add two number
@mcp.tool
def add(a:int, b:int) -> int :
    """
    Add two integer numbers.
    """
    return a + b

#START THE SERVER
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
    