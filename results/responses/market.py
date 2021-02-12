

class AddAlbumResponse(BaseResponse):
	market_album_id = None

class AddResponse(BaseResponse):
	market_item_id = None

class CreateCommentResponse(BaseResponse):
	

class DeleteCommentResponse(BaseResponse):
	

class GetAlbumByIdResponse(BaseResponse):
	count = None
	items = None

class GetAlbumsResponse(BaseResponse):
	count = None
	items = None

class GetByIdExtendedResponse(BaseResponse):
	count = None
	items = None

class GetByIdResponse(BaseResponse):
	count = None
	items = None

class GetCategoriesNewResponse(BaseResponse):
	items = None

class GetCategoriesResponse(BaseResponse):
	count = None
	items = None

class GetCommentsResponse(BaseResponse):
	count = None
	items = None

class GetGroupOrdersResponse(BaseResponse):
	count = None
	items = None

class GetOrderByIdResponse(BaseResponse):
	order = None

class GetOrderItemsResponse(BaseResponse):
	count = None
	items = None

class GetOrdersExtendedResponse(BaseResponse):
	count = None
	items = None
	groups = None

class GetOrdersResponse(BaseResponse):
	count = None
	items = None

class GetExtendedResponse(BaseResponse):
	count = None
	items = None

class GetResponse(BaseResponse):
	count = None
	items = None

class RestoreCommentResponse(BaseResponse):
	

class SearchExtendedResponse(BaseResponse):
	count = None
	items = None

class SearchResponse(BaseResponse):
	count = None
	items = None