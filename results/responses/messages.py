

class CreateChatResponse(BaseResponse):
	

class DeleteChatPhotoResponse(BaseResponse):
	message_id = None
	chat = None

class DeleteConversationResponse(BaseResponse):
	last_deleted_id = None

class DeleteResponse(BaseResponse):
	

class EditResponse(BaseResponse):
	

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

class GetChatChatIdsFieldsResponse(BaseResponse):
	

class GetChatChatIdsResponse(BaseResponse):
	

class GetChatFieldsResponse(BaseResponse):
	

class GetChatResponse(BaseResponse):
	

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

class GetLastActivityResponse(BaseResponse):
	

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

class GetLongPollServerResponse(BaseResponse):
	

class IsMessagesFromGroupAllowedResponse(BaseResponse):
	is_allowed = None

class JoinChatByInviteLinkResponse(BaseResponse):
	chat_id = None

class MarkAsImportantResponse(BaseResponse):
	

class PinResponse(BaseResponse):
	

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

class SendResponse(BaseResponse):
	

class SendUserIdsResponse(BaseResponse):
	

class SetChatPhotoResponse(BaseResponse):
	message_id = None
	chat = None