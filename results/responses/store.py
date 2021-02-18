from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class GetFavoriteStickersResponse(BaseResponse):
	response: Optional["GetFavoriteStickersResponseModel"] = None


class GetProductsResponse(BaseResponse):
	response: Optional["GetProductsResponseModel"] = None


class GetStickersKeywordsResponse(BaseResponse):
	response: Optional["GetStickersKeywordsResponseModel"] = None


GetFavoriteStickersResponseModel = List[BaseSticker]


GetProductsResponseModel = List[StoreProduct]


class GetStickersKeywordsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	dictionary: Optional["array"] = None
	chunks_count: Optional["integer"] = None
	chunks_hash: Optional["string"] = None

GetFavoriteStickersResponse.update_forward_refs()
GetProductsResponse.update_forward_refs()
GetStickersKeywordsResponse.update_forward_refs()