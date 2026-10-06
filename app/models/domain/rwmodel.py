import datetime

from pydantic import BaseModel, ConfigDict, field_serializer


def convert_datetime_to_realworld(dt: datetime.datetime) -> str:
    return dt.replace(tzinfo=datetime.timezone.utc).isoformat().replace("+00:00", "Z")


def convert_field_to_camel_case(string: str) -> str:
    return "".join(
        word if index == 0 else word.capitalize()
        for index, word in enumerate(string.split("_"))
    )


class RWModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=convert_field_to_camel_case)

    @field_serializer("created_at", "updated_at", when_used="json", check_fields=False)
    def serialize_datetime(self, value: datetime.datetime) -> str:
        return convert_datetime_to_realworld(value)
