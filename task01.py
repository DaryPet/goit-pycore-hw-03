
from datetime import datetime

def get_days_from_today(date):
    try:
       
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        
      
        current_date = datetime.today().date()
        
      
        delta = current_date - date_obj
        
        return delta.days
    except ValueError:
     
        return None
