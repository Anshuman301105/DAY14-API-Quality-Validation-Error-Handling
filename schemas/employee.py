from pydantic import BaseModel, Field, EmailStr, ConfigDict


# =========================================================
# Common fields
# =========================================================

class EmployeeBase(BaseModel):

    first_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee first name"
    )

    last_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=50,
        description="Employee last name"
    )

    email: EmailStr = Field(
        ...,
        max_length=100,
        description="Employee email"
    )

    phone_number: str | None = Field(
        default=None,
        pattern=r"^\d{10}$",
        description="10 digit employee phone number"
    )

    department: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Employee department"
    )


# =========================================================
# Create
# =========================================================

class EmployeeCreate(EmployeeBase):
    pass


# =========================================================
# Full Update
# =========================================================

class EmployeeUpdate(EmployeeBase):
    pass


# =========================================================
# Partial Update
# =========================================================

class EmployeePartialUpdate(BaseModel):

    first_name: str | None = Field(
        default=None,
        min_length=3,
        max_length=50
    )

    last_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=50
    )

    email: EmailStr | None = Field(
        default=None,
        max_length=100
    )

    phone_number: str | None = Field(
        default=None,
        pattern=r"^\d{10}$"
    )

    department: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
        description="Employee department"
    )


# =========================================================
# Response
# =========================================================

class EmployeeResponse(EmployeeBase):

    employee_id: int

    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# Paginated Response
# =========================================================

class EmployeeListResponse(BaseModel):

    page: int
    limit: int
    total: int
    total_pages: int
    employees: list[EmployeeResponse]