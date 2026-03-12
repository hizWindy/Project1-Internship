from .v1.router.interns_router import router as interns
from .v1.router.company_router import router as companies
from .v1.router.address_router import router as address
from .v1.router.apply_router import router as apply
from .v1.router.employer_router import router as employer
from .v1.router.job_router import router as jobs
from .v1.router.user_router import router as users
from .v1.router.question_router import router as questions
from .v1.router.project_router import router as projects
from .v1.router.availability_router import router as availabilities




routers = {"v1": (interns, companies, address, apply, employer, jobs, users, questions, projects, availabilities)}
