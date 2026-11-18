import sys

sys.path.insert(0, ".")
sys.stdout.reconfigure(encoding="utf-8")

from mcp import StdioServerParameters

from crewai_tools import MCPServerAdapter

from mcp_servers.playwright_mcp import build_playwright_args


def main():
    params = StdioServerParameters(
        command="npx",
        args=build_playwright_args(),
    )

    with MCPServerAdapter(params) as tools:
        # print("Available tools:")
        # for tool in tools:
        #     short_desc = tool.description.split("Tool Description:")[-1].strip()
        #     print(f" - {tool.name}: {short_desc}")

        # print(f"Total Number of tools: {len(tools)}")

        # Show the full description of browser_navigate
        nav_tool = tools["browser_navigate"]
        print("\n=== Full description for browser_navigate ===")
        print(nav_tool.description)
        print("=== End description ===\n")

        # Run browser_navigate manually
        print("Running browser_navigate ...")
        nav_result = nav_tool.run(url="https://qa-playground-automation-testing.onrender.com/")
        print(nav_result)
        print("Type of nav_result:", type(nav_result))

        # Show the full description of browser_snapshot
        snap_tool = tools["browser_snapshot"]
        print("\n=== Full description for browser_snapshot ===")
        print(snap_tool.description)
        print("=== End description ===\n")

        # Run browser_snapshot manually
        print("Running browser_snapshot ...")
        snap_result = snap_tool.run(target="", filename="", depth=10, boxes=False)
        print(snap_result)
        print("Type of snap_result:", type(snap_result))

        # # Example: navigate and snapshot manually
        # print("\nNavigating to example.com ...")
        # nav_result = tools["browser_navigate"].run(url="https://example.com")
        # print("Navigation result:", nav_result)

        # print("\nTaking snapshot ...")
        # snapshot_result = tools["browser_snapshot"].run(
        #     target="", filename="", depth=10, boxes=False
        # )
        # print(snapshot_result)


if __name__ == "__main__":
    main()
