from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class BoolResponse(BaseResponse):
	response: Optional["BoolResponseModel"] = None


class GetUploadServerResponse(BaseResponse):
	response: Optional["GetUploadServerResponseModel"] = None


class OkResponse(BaseResponse):
	response: Optional["OkResponseModel"] = None


BoolResponseModelModel = None


GetUploadServerResponseModelModel = None


OkResponseModelModel = None

BoolResponse.update_forward_refs()
GetUploadServerResponse.update_forward_refs()
OkResponse.update_forward_refs()
