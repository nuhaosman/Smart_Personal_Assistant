Smart Desktop Assistant – Python + LLM + Automation

How to Setup:
1. Install requirements: pip install -r requirements.txt
2. Add your OpenAI API key in llm_handler.py
3. Place nircmd.exe in the project folder (for volume control)
4. Run: python assistant.py or assistant_cli.py(if you are using codspaces)

How to Use:
- Type a natural language command like:
  "Search cute cats on Google"
  "Find music tutorials on YouTube"
  "Take a screenshot"
  "What is the capital of Japan?"

System Commands Supported:
- googleSearch
- youtubeSearch
- downloadMusic (placeholder)
- startWordProject
- screenShot
- lowerBrightness / higherBrightness
- highVolume / lowVolume

LLM Used:
- OpenAI GPT (via Python SDK)

