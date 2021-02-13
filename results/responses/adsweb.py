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
	categories: Optional["Array"] = None


class GetAdUnitCodeResponseModel(BaseResponse):
	html: Optional[str] = None


class GetAdUnitsResponseModel(BaseResponse):
	count: Optional[int] = None
	ad_units: Optional["Array"] = None


class GetFraudHistoryResponseModel(BaseResponse):
	count: Optional[int] = None
	entries: Optional["Array"] = None


class GetSitesResponseModel(BaseResponse):
	count: Optional[int] = None
	sites: Optional["Array"] = None


class GetStatisticsResponseModel(BaseResponse):
	next_page_id: Optional[str] = None
	items: Optional["Array"] = None

GetAdCategoriesResponse.update_forward_refs()
GetAdUnitCodeResponse.update_forward_refs()
GetAdUnitsResponse.update_forward_refs()
GetFraudHistoryResponse.update_forward_refs()
GetSitesResponse.update_forward_refs()
GetStatisticsResponse.update_forward_refs()
