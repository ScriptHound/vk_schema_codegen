from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class GetChairsResponse(BaseResponse):
	response: Optional["GetChairsResponseModel"] = None


class GetCitiesByIdResponse(BaseResponse):
	response: Optional["GetCitiesByIdResponseModel"] = None


class GetCitiesResponse(BaseResponse):
	response: Optional["GetCitiesResponseModel"] = None


class GetCountriesByIdResponse(BaseResponse):
	response: Optional["GetCountriesByIdResponseModel"] = None


class GetCountriesResponse(BaseResponse):
	response: Optional["GetCountriesResponseModel"] = None


class GetFacultiesResponse(BaseResponse):
	response: Optional["GetFacultiesResponseModel"] = None


class GetMetroStationsByIdResponse(BaseResponse):
	response: Optional["GetMetroStationsByIdResponseModel"] = None


class GetMetroStationsResponse(BaseResponse):
	response: Optional["GetMetroStationsResponseModel"] = None


class GetRegionsResponse(BaseResponse):
	response: Optional["GetRegionsResponseModel"] = None


class GetSchoolClassesResponse(BaseResponse):
	response: Optional["GetSchoolClassesResponseModel"] = None


class GetSchoolsResponse(BaseResponse):
	response: Optional["GetSchoolsResponseModel"] = None


class GetUniversitiesResponse(BaseResponse):
	response: Optional["GetUniversitiesResponseModel"] = None


class GetChairsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


GetCitiesByIdResponseModelModel = array


class GetCitiesResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


GetCountriesByIdResponseModelModel = array


class GetCountriesResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetFacultiesResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


GetMetroStationsByIdResponseModelModel = array


class GetMetroStationsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetRegionsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


GetSchoolClassesResponseModelModel = array


class GetSchoolsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetUniversitiesResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None

GetChairsResponse.update_forward_refs()
GetCitiesByIdResponse.update_forward_refs()
GetCitiesResponse.update_forward_refs()
GetCountriesByIdResponse.update_forward_refs()
GetCountriesResponse.update_forward_refs()
GetFacultiesResponse.update_forward_refs()
GetMetroStationsByIdResponse.update_forward_refs()
GetMetroStationsResponse.update_forward_refs()
GetRegionsResponse.update_forward_refs()
GetSchoolClassesResponse.update_forward_refs()
GetSchoolsResponse.update_forward_refs()
GetUniversitiesResponse.update_forward_refs()
