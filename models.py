# ================================================================================
# University of Saskatchewan
# Edwards School of Business
# 25 Campus Drive
# Nutrien Centre
# Saskatoon, SK
# S7N 5A7
# 306-966-4785
# Fax
# 306-966-5408
# Website : 
# http://www.edwards.usask.ca/
# Campuses: 
# University 
# Dowtown 
# Accreditations:
# AACSB
# ================================================================================

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, registry, relationship

Base = declarative_base()

class College(Base):
    __tablename__ = 'college'

    id = Column(Integer, primary_key=True)
    university_name = Column(String(255))
    college_name = Column(String(255))
    mailing_address_1 = Column(String(255))
    mailing_address_2 = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zip = Column(String(20))
    phone = Column(String(20))
    fax = Column(String(20))
    url = Column(String(255))
    dean_name = Column(String(255))
    dean_email = Column(String(2550))

    def __repr__(self) -> str:
        return f"{self.college_name!r}"

