from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class ChangePasswordResponse(BaseResponse):
	response: Optional["ChangePasswordResponseModel"] = None


class GetActiveOffersResponse(BaseResponse):
	response: Optional["GetActiveOffersResponseModel"] = None


class GetAppPermissionsResponse(BaseResponse):
	response: Optional["GetAppPermissionsResponseModel"] = None


class GetBannedResponse(BaseResponse):
	response: Optional["GetBannedResponseModel"] = None


class GetCountersResponse(BaseResponse):
	response: Optional["GetCountersResponseModel"] = None


class GetInfoResponse(BaseResponse):
	response: Optional["GetInfoResponseModel"] = None


class GetProfileInfoResponse(BaseResponse):
	response: Optional["GetProfileInfoResponseModel"] = None


class GetPushSettingsResponse(BaseResponse):
	response: Optional["GetPushSettingsResponseModel"] = None


class SaveProfileInfoResponse(BaseResponse):
	response: Optional["SaveProfileInfoResponseModel"] = None


class ChangePasswordResponseModel(BaseResponse):
	token: Optional[str] = None
	secret: Optional[str] = None


class GetActiveOffersResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


GetAppPermissionsResponseModelModel = None


class GetBannedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None
	profiles: Optional["Array"] = None
	groups: Optional["Array"] = None


GetCountersResponseModelModel = None


GetInfoResponseModelModel = None


GetProfileInfoResponseModelModel = None


GetPushSettingsResponseModelModel = None


class SaveProfileInfoResponseModel(BaseResponse):
	changed = None
	name_request = None

ChangePasswordResponse.update_forward_refs()
GetActiveOffersResponse.update_forward_refs()
GetAppPermissionsResponse.update_forward_refs()
GetBannedResponse.update_forward_refs()
GetCountersResponse.update_forward_refs()
GetInfoResponse.update_forward_refs()
GetProfileInfoResponse.update_forward_refs()
GetPushSettingsResponse.update_forward_refs()
SaveProfileInfoResponse.update_forward_refs()
