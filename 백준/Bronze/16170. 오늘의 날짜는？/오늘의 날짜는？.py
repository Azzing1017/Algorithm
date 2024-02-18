from datetime import datetime, timezone

n = datetime.now(timezone.utc)
print(n.year)
print(n.month)
print(n.day)
