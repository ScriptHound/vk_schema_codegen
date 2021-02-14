from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class GetHintsResponse(BaseResponse):
	response: Optional["GetHintsResponseModel"] = None


class GetHintsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	suggested_queries: Optional["array"] = None

GetHintsResponse.update_forward_refs()