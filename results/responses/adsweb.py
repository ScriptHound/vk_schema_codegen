from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class GetAdCategoriesResponse(BaseResponse):
	response: Optional["GetAdCategoriesResponseModel"] = None


class GetAdUnitCodeResponse(BaseResponse):
	response: Optional["GetAdUnitCodeResponseModel"] = None


class GetAdUnitsResponse(BaseResponse):
	response: Optional["GetAdUnitsResponseModel"] = None


class GetFraudHistoryResponse(BaseResponse):
	response: Optional["GetFraudHistoryResponseModel"] = None


class GetSitesResponse(BaseResponse):
	response: Optional["GetSitesResponseModel"] = None


class GetStatisticsResponse(BaseResponse):
	response: Optional["GetStatisticsResponseModel"] = None


class GetAdCategoriesResponseModel(BaseResponse):
	categories: Optional["array"] = None


class GetAdUnitCodeResponseModel(BaseResponse):
	html: Optional["string"] = None


class GetAdUnitsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	ad_units: Optional["array"] = None


class GetFraudHistoryResponseModel(BaseResponse):
	count: Optional["integer"] = None
	entries: Optional["array"] = None


class GetSitesResponseModel(BaseResponse):
	count: Optional["integer"] = None
	sites: Optional["array"] = None


class GetStatisticsResponseModel(BaseResponse):
	next_page_id: Optional["string"] = None
	items: Optional["array"] = None

GetAdCategoriesResponse.update_forward_refs()
GetAdUnitCodeResponse.update_forward_refs()
GetAdUnitsResponse.update_forward_refs()
GetFraudHistoryResponse.update_forward_refs()
GetSitesResponse.update_forward_refs()
GetStatisticsResponse.update_forward_refs()