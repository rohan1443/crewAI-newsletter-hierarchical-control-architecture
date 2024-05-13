# CrewAI-newsletter-hierarchical-control-architecture

## CrewAI concept
CrewAi by default supports the task management process in a sequential way, but have recently launched a feature of hierarchical orchestration mechanism of task management/execution ensuring goals are achieved efficiently and cohesively. These processes enable individual agents to function as a coordinated unit, similar to project management in human teams.

## About
Demonstrating the power of multi-agent based application, this is a CREWAI python based application that is used to fetch the latest top 5 last 24 hrs AI related most relevant news from the google search api using Serper and generate a Newsletter in a markdown format file.

### CrewAi based app Architecture 

[miro link](https://miro.com/app/board/uXjVKKYwQFc=/)

<img width="1060" alt="image" src="https://github.com/rohan1443/crewAI-newsletter-hierarchical-control-architecture/assets/12879983/7d693d40-ff27-4c3b-bf0b-a5eafa622da5">


## Feature
- async task execution
- task delegation and process management execution
- expected output
- manager LLM
  
## Tech used:
- CrewAI (AGENT, TASK, TOOLS)
- Serper API
- OpenAI
- Langchain
- Python

## Goal definition and Output
- Creation of a AI newsLetter 
In the below snapshot a glimpse of the code where multiple agents has been created to execute a specific task and also provided with customised tool configured with serper to scrap and search the internet for the required information and as per the task goal defined.

- Agent Creation and configuration
  <br/>
  <img width="1133" alt="image" src="https://github.com/rohan1443/crewAI-newsletter-hierarchical-control-architecture/assets/12879983/55401d8e-ea31-43c6-90c5-d754a3d75aa7">
<br/>
- Output
  <br/>
<img width="1235" alt="image" src="https://github.com/rohan1443/crewAI-newsletter-hierarchical-control-architecture/assets/12879983/2e1aa5b1-0984-4a40-a5d3-397d620f0cbb">
<br/>
- Markdown format file generated snapshot
 <br/>
 
![image](https://github.com/rohan1443/crewAI-newsletter-hierarchical-control-architecture/assets/12879983/7fc22885-da49-459f-98f1-994c0a4583f0)

<br/>

