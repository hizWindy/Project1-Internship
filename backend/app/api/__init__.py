from .v1.router.interns_router import router as interns
from .v1.router.company_router import router as companies

routers = {"v1": (interns, companies)}
