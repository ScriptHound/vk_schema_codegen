


class CreateChatResponse(BaseResponse):
	response = None


class DeleteChatPhotoResponse(BaseResponse):
	response = None


class DeleteConversationResponse(BaseResponse):
	response = None


class DeleteResponse(BaseResponse):
	response = None


class EditResponse(BaseResponse):
	response = None


class GetByConversationMessageIdResponse(BaseResponse):
	response = None


class GetByIdExtendedResponse(BaseResponse):
	response = None


class GetByIdResponse(BaseResponse):
	response = None


class GetChatPreviewResponse(BaseResponse):
	response = None


class GetChatChatIdsFieldsResponse(BaseResponse):
	response = None


class GetChatChatIdsResponse(BaseResponse):
	response = None


class GetChatFieldsResponse(BaseResponse):
	response = None


class GetChatResponse(BaseResponse):
	response = None


class GetConversationMembersResponse(BaseResponse):
	response = None


class GetConversationsByIdExtendedResponse(BaseResponse):
	response = None


class GetConversationsByIdResponse(BaseResponse):
	response = None


class GetConversationsResponse(BaseResponse):
	response = None


class GetHistoryAttachmentsResponse(BaseResponse):
	response = None


class GetHistoryExtendedResponse(BaseResponse):
	response = None


class GetHistoryResponse(BaseResponse):
	response = None


class GetImportantMessagesExtendedResponse(BaseResponse):
	response = None


class GetImportantMessagesResponse(BaseResponse):
	response = None


class GetIntentUsersResponse(BaseResponse):
	response = None


class GetInviteLinkResponse(BaseResponse):
	response = None


class GetLastActivityResponse(BaseResponse):
	response = None


class GetLongPollHistoryResponse(BaseResponse):
	response = None


class GetLongPollServerResponse(BaseResponse):
	response = None


class IsMessagesFromGroupAllowedResponse(BaseResponse):
	response = None


class JoinChatByInviteLinkResponse(BaseResponse):
	response = None


class MarkAsImportantResponse(BaseResponse):
	response = None


class PinResponse(BaseResponse):
	response = None


class SearchConversationsExtendedResponse(BaseResponse):
	response = None


class SearchConversationsResponse(BaseResponse):
	response = None


class SearchExtendedResponse(BaseResponse):
	response = None


class SearchResponse(BaseResponse):
	response = None


class SendResponse(BaseResponse):
	response = None


class SendUserIdsResponse(BaseResponse):
	response = None


class SetChatPhotoResponse(BaseResponse):
	response = None


CreateChatResponseModel = None


class DeleteChatPhotoResponse(BaseResponse):
	message_id = None
	chat = None


class DeleteConversationResponse(BaseResponse):
	last_deleted_id = None


DeleteResponseModel = typing.Dict[str, int]


EditResponseModel = None


class GetByConversationMessageIdResponse(BaseResponse):
	count = None
	items = None


class GetByIdExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None


class GetByIdResponse(BaseResponse):
	count = None
	items = None


class GetChatPreviewResponse(BaseResponse):
	preview = None
	profiles = None


GetChatChatIdsFieldsResponseModel = array


GetChatChatIdsResponseModel = array


GetChatFieldsResponseModel = None


GetChatResponseModel = None


class GetConversationMembersResponse(BaseResponse):
	count = None
	items = None
	chat_restrictions = None
	profiles = None
	groups = None


class GetConversationsByIdExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None


class GetConversationsByIdResponse(BaseResponse):
	count = None
	items = None


class GetConversationsResponse(BaseResponse):
	count = None
	unread_count = None
	items = None
	profiles = None
	groups = None


class GetHistoryAttachmentsResponse(BaseResponse):
	items = None
	next_from = None


class GetHistoryExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None
	conversations = None


class GetHistoryResponse(BaseResponse):
	count = None
	items = None


class GetImportantMessagesExtendedResponse(BaseResponse):
	messages = None
	profiles = None
	groups = None
	conversations = None


class GetImportantMessagesResponse(BaseResponse):
	messages = None
	profiles = None
	groups = None
	conversations = None


class GetIntentUsersResponse(BaseResponse):
	count = None
	items = None
	profiles = None


class GetInviteLinkResponse(BaseResponse):
	link = None


GetLastActivityResponseModel = None


class GetLongPollHistoryResponse(BaseResponse):
	history = None
	messages = None
	credentials = None
	profiles = None
	groups = None
	chats = None
	new_pts = None
	from_pts = None
	more = None
	conversations = None


GetLongPollServerResponseModel = None


class IsMessagesFromGroupAllowedResponse(BaseResponse):
	is_allowed = None


class JoinChatByInviteLinkResponse(BaseResponse):
	chat_id = None


MarkAsImportantResponseModel = array


PinResponseModel = None


class SearchConversationsExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None


class SearchConversationsResponse(BaseResponse):
	count = None
	items = None


class SearchExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None
	conversations = None


class SearchResponse(BaseResponse):
	count = None
	items = None


SendResponseModel = None


SendUserIdsResponseModel = array


class SetChatPhotoResponse(BaseResponse):
	message_id = None
	chat = None