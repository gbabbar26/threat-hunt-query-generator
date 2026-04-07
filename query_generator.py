import anthropic
import os
from datetime import datetime

timestamp=datetime.now().strftime("%Y-%m-%d-%H-%M") 
try:
	client=anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
except Exception as e:
	print("API KEY Not found/failed/wrong due to connectivity issues")
	print(f"Error details: {e}")
	exit()

print("Threat Hunt Query Generator")
threat = input("Describe the suspicious behaviour: ")
siem=input("What SIEM tool do you want to use: Splunk, MS Sentinel, Elastic?")

def generate_query(threat, siem):
	try:
		
		prompt="You are an expert Threat Hunter whose job is to analyse suspicious behavior. This is a suspicious behaviour, analyse it and generate a necessary " + siem + "Query for this. \n\n" + threat
		message=client.messages.create(
			model="claude-sonnet-4-20250514",
			max_tokens=1024,
			messages=[
				{"role":"user", "content":prompt}
		])
		return message.content[0].text
	except Exception as e:
		print(f"Error Details: {e}")
		print("This threat failed to analysed, moving onto next. Check Manually")
		return None

result=generate_query(threat, siem)

if result:	
	print(result)
	threat_report=f"query_{timestamp}.txt"
	with open (threat_report, "w", encoding="utf-8") as f:
		f.write(f"Threat: {threat}\n")
		f.write(f"SIEM: {siem}\n")
		f.write(f"Generated Query: {result}\n")
		f.write(f"Timestamp: {timestamp}\n")
		
	print(f"Done! Report saved to {threat_report}")
