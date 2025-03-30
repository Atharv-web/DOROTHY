from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig,CrawlerRunConfig
import asyncio
from crewai.tools import BaseTool


class WebScraperTool(BaseTool):

    name: str = "Web Scraper"
    description: str = "Scrapes the data , media, links, and any other information present in the provided URL"

    async def web_data_gatherer(self):
        url = input("Enter a URL: ")
        browser_config = BrowserConfig()
        crawler_config = CrawlerRunConfig()

        async with AsyncWebCrawler(config=browser_config) as crawler:
            crawler_result = await crawler.arun(
                url = url,
                config= crawler_config,
            )
        
            output = {
                "media": crawler_result.media,
                "all_links": crawler_result.links,
                "raw_markdown_data": crawler_result.markdown.raw_markdown,
                "most_relevant_content": crawler_result.markdown.fit_markdown
            }
            return output
        
    def _run(self) -> dict:
        return asyncio.run(self.web_data_gatherer())
    
# tool = WebScraperTool()
# a = tool._run()
# print(a)