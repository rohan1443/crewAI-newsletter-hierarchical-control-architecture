from crewai import Crew
from crewai.process import Process
from langchain_openai import ChatOpenAI
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from file_io import save_markdown
from dotenv import load_dotenv

load_dotenv()

OpenAIGPT4 = ChatOpenAI(
    model="gpt-4"
)

agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()
# setting up agents

editor = agents.editor_agent()
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
newsletter_compiler = agents.newsletter_compiler_agent()

# setting up tasks

fetch_news_task = tasks.fetch_news_task(news_fetcher)
analyze_news_task = tasks.analyze_news_task(
    news_analyzer, [fetch_news_task])  # passing multiple items in a context
compile_news_task = tasks.compile_newsletter_task(
    newsletter_compiler, [analyze_news_task], save_markdown)

# setting up tools


crew = Crew(
    agents=[editor, news_analyzer, news_fetcher, newsletter_compiler],
    tasks=[fetch_news_task, analyze_news_task, compile_news_task],
    process=Process.hierarchical,
    manager_llm=OpenAIGPT4
)

# kickoff the crew
results = crew.kickoff()

print('Crew work results \n', results)
