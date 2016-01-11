'''
Created on Nov 27, 2015

@author: SG0946321
'''
from com.sabre.api.des.rest.activities.LeadPriceCalendarActivity import LeadPriceCalendarActivity
from com.sabre.api.des.workflow.Workflow import Workflow

workflow = Workflow(LeadPriceCalendarActivity())
sharedContext = workflow.runWorkflow()
print("---------------------- RESULTS --------------------------")
print(sharedContext.leadPriceCalendarResult.text)
print(sharedContext.instaFlightResult.text)
print(sharedContext.bargainFinderMaxResult.text)