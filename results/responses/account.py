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
	token: Optional["string"] = None
	secret: Optional["string"] = None


class GetActiveOffersResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


GetAppPermissionsResponseModel = int


class GetBannedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


GetCountersResponseModel = Optional[Accountaccountcounters]


GetInfoResponseModel = Optional[Accountinfo]


GetProfileInfoResponseModel = Optional[Accountusersettings]


GetPushSettingsResponseModel = Optional[Accountpushsettings]


class SaveProfileInfoResponseModel(BaseResponse):
	changed: Optional["baseboolint"] = None
	name_request: Optional["accountnamerequest"] = None

ChangePasswordResponse.update_forward_refs()
GetActiveOffersResponse.update_forward_refs()
GetAppPermissionsResponse.update_forward_refs()
GetBannedResponse.update_forward_refs()
GetCountersResponse.update_forward_refs()
GetInfoResponse.update_forward_refs()
GetProfileInfoResponse.update_forward_refs()
GetPushSettingsResponse.update_forward_refs()
SaveProfileInfoResponse.update_forward_refs()