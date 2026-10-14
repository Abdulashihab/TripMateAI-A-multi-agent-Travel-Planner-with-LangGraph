from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

#res =tavily_search("best hotels in india")
#print(res)


res = search_flights("plan 7 days nepal trip from bangladesh")
print(res)