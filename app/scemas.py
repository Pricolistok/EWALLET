from pydantic import Field, field_validator, BaseModel


class OperationRequest(BaseModel):
    wallet_name: str = Field(..., max_length=127)
    amount: float = Field(..., ge=0)
    description: str | None = Field(None, max_length=255)

    @field_validator("wallet_name")
    def wallet_name_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Name is mpty")
        return v


class OperationCreateWallet(BaseModel):
    wallet_name: str = Field(..., max_length=127)
    init_balance: float = Field(..., ge=0)


    @field_validator("wallet_name")
    def wallet_name_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Name is mpty")
        return v