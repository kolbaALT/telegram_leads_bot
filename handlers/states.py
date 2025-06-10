from aiogram.fsm.state import StatesGroup, State

class LeadForm(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_request = State()
