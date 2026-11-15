# The Master Plan
 I am writing this document to layout how I plan to build the tool in mind. This is not set in stone as no plan is perfect. This document will layout the inital plan and then log the changes to the plan. 

## Goal
The goal is to build a chat based tool that is targeted at MLB broadcasters. The tool will use Claude and a mixture of back end tools to all the bot to present data. 

The end goal would be a tool that can take questions like... 
- "How does Clement do against right handed batters?"
- "How has Aaron Judge last ten at bats compared to the rest of the season and career?"
- "Any fun social media trends or topics about Kirk?" 
And provide actual data/sources for the broadcaster to talk about. 

## Intial Plan

### AI Structure
The actual AI will be all Claude API calls with multiple different steps to help build the final result. Below is the 3 steps/ agents that will be needed.

1. Reaserch Agent
This agent will interpet the question being given by the user. It will need to plan what type of data is needed and how it should access it. 
2. Writing/Presentation Agent 
This agent will take the data given by the Reaserch agent and put it into proper UI. The end goal should not just be a text return but instead a proper report with tables of data and strectured text. 

### Front End
Front end will be a react based webpage using Fast API to connect to the backend. 

For the final end result the AI will need widgets/components that it can use to build a response. Something like a table component, bullet points, or maybe even charts would be a great way to present more information. 

### Back End
Back end will be a mixture of SQL server (Docker) and direct connections to MLB api using [MLB Stats API](https://github.com/toddrob99/MLB-StatsAPI) by [Todd Roberts](https://github.com/toddrob99). 

The SQL solution can be the historic data. This way we can store pitch by pitch data and aggergate it using SQL for the specific question we want. 

The latest data should be using the API call so that it can get live MLB data and compare to the historic data if need.