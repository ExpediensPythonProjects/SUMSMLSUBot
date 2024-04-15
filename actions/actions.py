from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet



class ActionClearSlot(Action):
    def name(self):
        return 'action_restart_conversation'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = [
            {"title": "Result Related Query", "payload": 'result_related_query'},
            {"title": "Frequently Asked Questions", "payload": 'frequently_asked_questions'},
        ]

        dispatcher.utter_message(text="Greetings and Welcome to SUMSMLSU! I am your Virtual Assistant, prepared to assist you. To get started, kindly select an option from the menu below", buttons=buttons)
        return []
    

class ActionExitConversation(Action):
    def name(self):
        return 'action_exit_conversation'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Bye, Have a Nice Day.")
        return []



class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = [
            {"title": "Result Related Query", "payload": 'result_related_query'},
            {"title": "Frequently Asked Questions", "payload": 'frequently_asked_questions'},
        ]

        dispatcher.utter_message(text="I Apologize for the Confusion. I'm Here to Assist You with Something Similar To",  buttons=buttons)

        return []