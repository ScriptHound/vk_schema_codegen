

class GetCatalogResponse(BaseResponse):
	count = None
	items = None
	profiles = None

class GetFriendsListResponse(BaseResponse):
	count = None
	items = None

class GetLeaderboardExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None

class GetLeaderboardResponse(BaseResponse):
	count = None
	items = None

class GetMiniAppPoliciesResponse(BaseResponse):
	privacy_policy = None
	terms = None

class GetScopesResponse(BaseResponse):
	count = None
	items = None

class GetScoreResponse(BaseResponse):
	

class GetResponse(BaseResponse):
	count = None
	items = None

class ImageUploadResponse(BaseResponse):
	hash = None
	image = None

class SendRequestResponse(BaseResponse):
	