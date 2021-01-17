class AccountOffer:
	"""VK Object AccountOffer

	description - Offer description
	id - Offer ID
	img - URL of the preview image
	instruction - Instruction how to process the offer
	instruction_html - Instruction how to process the offer (HTML format)
	price - Offer price
	short_description - Offer short description
	tag - Offer tag
	title - Offer title
	currency_amount - Currency amount
	link_id - Link id
	link_type - Link type
	"""
	description = None
	id = None
	img = None
	instruction = None
	instruction_html = None
	price = None
	short_description = None
	tag = None
	title = None
	currency_amount = None
	link_id = None
	link_type = None
class AccountPushConversAtionsItem:
	"""VK Object AccountPushConversAtionsItem

	disabled_until - Time until that notifications are disabled in seconds
	peer_id - Peer ID
	sound - Information whether the sound are enabled
	"""
	disabled_until = None
	peer_id = None
	sound = None
class AdsClient:
	"""VK Object AdsClient

	all_limit - Client's total limit, rubles
	day_limit - Client's day limit, rubles
	id - Client ID
	name - Client name
	"""
	all_limit = None
	day_limit = None
	id = None
	name = None
class AdsFloodStAts:
	"""VK Object AdsFloodStAts

	left - Requests left
	refresh - Time to refresh in seconds
	"""
	left = None
	refresh = None
class AdsLinkStAtus:
	"""VK Object AdsLinkStAtus

	description - Reject reason
	redirect_url - URL
	status - Link status
	"""
	description = None
	redirect_url = None
	status = None
class AdsLookAlikeRequestSAveAudienceLevel:
	"""VK Object AdsLookAlikeRequestSAveAudienceLevel

	level - Save audience level id, which is used in save audience queries
	audience_count - Saved audience audience size for according level
	"""
	level = None
	audience_count = None
class AdsMusiciAn:
	"""VK Object AdsMusiciAn

	id - Targeting music artist ID
	name - Music artist name
	avatar - Music artist photo
	"""
	id = None
	name = None
	avatar = None
class AdsPArAgrAphs:
	"""VK Object AdsPArAgrAphs

	paragraph - Rules paragraph
	"""
	paragraph = None
class AdsPromotedPostReAch:
	"""VK Object AdsPromotedPostReAch

	hide - Hides amount
	id - Object ID from 'ids' parameter
	join_group - Community joins
	links - Link clicks
	reach_subscribers - Subscribers reach
	reach_total - Total reach
	report - Reports amount
	to_group - Community clicks
	unsubscribe - 'Unsubscribe' events amount
	video_views_100p - Video views for 100 percent
	video_views_25p - Video views for 25 percent
	video_views_3s - Video views for 3 seconds
	video_views_50p - Video views for 50 percent
	video_views_75p - Video views for 75 percent
	video_views_start - Video starts
	"""
	hide = None
	id = None
	join_group = None
	links = None
	reach_subscribers = None
	reach_total = None
	report = None
	to_group = None
	unsubscribe = None
	video_views_100p = None
	video_views_25p = None
	video_views_3s = None
	video_views_50p = None
	video_views_75p = None
	video_views_start = None
class AdsStAtsAge:
	"""VK Object AdsStAtsAge

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	value - Age interval
	"""
	clicks_rate = None
	impressions_rate = None
	value = None
class AdsStAtsCities:
	"""VK Object AdsStAtsCities

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	name - City name
	value - City ID
	"""
	clicks_rate = None
	impressions_rate = None
	name = None
	value = None
class AdsStAtsFormAt:
	"""VK Object AdsStAtsFormAt

	clicks - Clicks number
	day - Day as YYYY-MM-DD
	impressions - Impressions number
	join_rate - Events number
	month - Month as YYYY-MM
	overall - 1 if period=overall
	reach - Reach 
	spent - Spent funds
	video_clicks_site - Clickthoughs to the advertised site
	video_views - Video views number
	video_views_full - Video views (full video)
	video_views_half - Video views (half of video)
	"""
	clicks = None
	day = None
	impressions = None
	join_rate = None
	month = None
	overall = None
	reach = None
	spent = None
	video_clicks_site = None
	video_views = None
	video_views_full = None
	video_views_half = None
class AdsStAtsSexAge:
	"""VK Object AdsStAtsSexAge

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	value - Sex and age interval
	"""
	clicks_rate = None
	impressions_rate = None
	value = None
class AdsTArgStAts:
	"""VK Object AdsTArgStAts

	audience_count - Audience
	recommended_cpc - Recommended CPC value for 50% reach (old format)
	recommended_cpm - Recommended CPM value for 50% reach (old format)
	recommended_cpc_50 - Recommended CPC value for 50% reach
	recommended_cpm_50 - Recommended CPM value for 50% reach
	recommended_cpc_70 - Recommended CPC value for 70% reach
	recommended_cpm_70 - Recommended CPM value for 70% reach
	recommended_cpc_90 - Recommended CPC value for 90% reach
	recommended_cpm_90 - Recommended CPM value for 90% reach
	"""
	audience_count = None
	recommended_cpc = None
	recommended_cpm = None
	recommended_cpc_50 = None
	recommended_cpm_50 = None
	recommended_cpc_70 = None
	recommended_cpm_70 = None
	recommended_cpc_90 = None
	recommended_cpm_90 = None
class AdsTArgSuggestions:
	"""VK Object AdsTArgSuggestions

	id - Object ID
	name - Object name
	"""
	id = None
	name = None
class AdsTArgSuggestionsCities:
	"""VK Object AdsTArgSuggestionsCities

	id - Object ID
	name - Object name
	parent - Parent object
	"""
	id = None
	name = None
	parent = None
class AdsTArgSuggestionsRegions:
	"""VK Object AdsTArgSuggestionsRegions

	id - Object ID
	name - Object name
	type - Object type
	"""
	id = None
	name = None
	type = None
class AdsTArgetGroup:
	"""VK Object AdsTArgetGroup

	audience_count - Audience
	domain - Site domain
	id - Group ID
	lifetime - Number of days for user to be in group
	name - Group name
	pixel - Pixel code
	"""
	audience_count = None
	domain = None
	id = None
	lifetime = None
	name = None
	pixel = None
class AppsLeAderboArd:
	"""VK Object AppsLeAderboArd

	level - Level
	points - Points number
	score - Score number
	user_id - User ID
	"""
	level = None
	points = None
	score = None
	user_id = None
class AppsScope:
	"""VK Object AppsScope

	name - Scope name
	title - Scope title
	"""
	name = None
	title = None
class AudioAudio:
	"""VK Object AudioAudio

	access_key - Access key for the audio
	artist - Artist name
	id - Audio ID
	owner_id - Audio owner's ID
	title - Title
	url - URL of mp3 file
	duration - Duration in seconds
	date - Date when uploaded
	album_id - Album ID
	genre_id - Genre ID
	performer - Performer name
	"""
	access_key = None
	artist = None
	id = None
	owner_id = None
	title = None
	url = None
	duration = None
	date = None
	album_id = None
	genre_id = None
	performer = None
class BaseCity:
	"""VK Object BaseCity

	id - City ID
	title - City title
	"""
	id = None
	title = None
class BaseCountry:
	"""VK Object BaseCountry

	id - Country ID
	title - Country title
	"""
	id = None
	title = None
class BaseCropPhotoCrop:
	"""VK Object BaseCropPhotoCrop

	x - Coordinate X of the left upper corner
	y - Coordinate Y of the left upper corner
	x2 - Coordinate X of the right lower corner
	y2 - Coordinate Y of the right lower corner
	"""
	x = None
	y = None
	x2 = None
	y2 = None
class BaseCropPhotoRect:
	"""VK Object BaseCropPhotoRect

	x - Coordinate X of the left upper corner
	y - Coordinate Y of the left upper corner
	x2 - Coordinate X of the right lower corner
	y2 - Coordinate Y of the right lower corner
	"""
	x = None
	y = None
	x2 = None
	y2 = None
class BaseGradientPoint:
	"""VK Object BaseGradientPoint

	color - Hex color code without #
	position - Point position
	"""
	color = None
	position = None
class BaseLikes:
	"""VK Object BaseLikes

	count - Likes number
	user_likes - Information whether current user likes the photo
	"""
	count = None
	user_likes = None
class BaseLikesInfo:
	"""VK Object BaseLikesInfo

	can_like - Information whether current user can like the post
	can_publish - Information whether current user can repost
	count - Likes number
	user_likes - Information whether current uer has liked the post
	"""
	can_like = None
	can_publish = None
	count = None
	user_likes = None
class BaseLinkApplicationStore:
	"""VK Object BaseLinkApplicationStore

	id - Store Id
	name - Store name
	"""
	id = None
	name = None
class BaseLinkRating:
	"""VK Object BaseLinkRating

	reviews_count - Count of reviews
	stars - Count of stars
	"""
	reviews_count = None
	stars = None
class BaseMessageError:
	"""VK Object BaseMessageError

	code - Error code
	description - Error message
	"""
	code = None
	description = None
class BaseOBject:
	"""VK Object BaseOBject

	id - Object ID
	title - Object title
	"""
	id = None
	title = None
class BaseOBjectCount:
	"""VK Object BaseOBjectCount

	count - Items count
	"""
	count = None
class BaseOBjectWithName:
	"""VK Object BaseOBjectWithName

	id - Object ID
	name - Object name
	"""
	id = None
	name = None
class BasePlace:
	"""VK Object BasePlace

	address - Place address
	checkins - Checkins number
	city - City name
	country - Country name
	created - Date of the place creation in Unixtime
	icon - URL of the place's icon
	id - Place ID
	latitude - Place latitude
	longitude - Place longitude
	title - Place title
	type - Place type
	"""
	address = None
	checkins = None
	city = None
	country = None
	created = None
	icon = None
	id = None
	latitude = None
	longitude = None
	title = None
	type = None
class BaseRepostsInfo:
	"""VK Object BaseRepostsInfo

	count - Total reposts counter. Sum of wall and mail reposts counters
	wall_count - Wall reposts counter
	mail_count - Mail reposts counter
	user_reposted - Information whether current user has reposted the post
	"""
	count = None
	wall_count = None
	mail_count = None
	user_reposted = None
class BaseRequestParam:
	"""VK Object BaseRequestParam

	key - Parameter name
	value - Parameter value
	"""
	key = None
	value = None
class BaseStickerAnimation:
	"""VK Object BaseStickerAnimation

	type - Type of animation script
	url - URL of animation script
	"""
	type = None
	url = None
class BaseUploadServer:
	"""VK Object BaseUploadServer

	upload_url - Upload URL
	"""
	upload_url = None
class BaseUserId:
	"""VK Object BaseUserId

	user_id - User ID
	"""
	user_id = None
class BoardTopic:
	"""VK Object BoardTopic

	comments - Comments number
	created - Date when the topic has been created in Unixtime
	created_by - Creator ID
	id - Topic ID
	is_closed - Information whether the topic is closed
	is_fixed - Information whether the topic is fixed
	title - Topic title
	updated - Date when the topic has been updated in Unixtime
	updated_by - ID of user who updated the topic
	"""
	comments = None
	created = None
	created_by = None
	id = None
	is_closed = None
	is_fixed = None
	title = None
	updated = None
	updated_by = None
class DatabaseFaculty:
	"""VK Object DatabaseFaculty

	id - Faculty ID
	title - Faculty title
	"""
	id = None
	title = None
class DatabaseRegion:
	"""VK Object DatabaseRegion

	id - Region ID
	title - Region title
	"""
	id = None
	title = None
class DatabaseSchool:
	"""VK Object DatabaseSchool

	id - School ID
	title - School title
	"""
	id = None
	title = None
class DatabaseStation:
	"""VK Object DatabaseStation

	city_id - City ID
	color - Hex color code without #
	id - Station ID
	name - Station name
	"""
	city_id = None
	color = None
	id = None
	name = None
class DatabaseUniversity:
	"""VK Object DatabaseUniversity

	id - University ID
	title - University title
	"""
	id = None
	title = None
class DocsDocPreviewGraffiti:
	"""VK Object DocsDocPreviewGraffiti

	src - Graffiti file URL
	width - Graffiti width
	height - Graffiti height
	"""
	src = None
	width = None
	height = None
class DocsDocPreviewViDeo:
	"""VK Object DocsDocPreviewViDeo

	src - Video URL
	width - Video's width in pixels
	height - Video's height in pixels
	file_size - Video file size in bites
	"""
	src = None
	width = None
	height = None
	file_size = None
class DocsDocTypes:
	"""VK Object DocsDocTypes

	id - Doc type ID
	name - Doc type title
	count - Number of docs
	"""
	id = None
	name = None
	count = None
class EvEntsEvEntAttach:
	"""VK Object EvEntsEvEntAttach

	address - address of event
	button_text - text of attach
	friends - array of friends ids
	id - event ID
	is_favorite - is favorite
	member_status - Current user's member status
	text - text of attach
	time - event start time
	"""
	address = None
	button_text = None
	friends = None
	id = None
	is_favorite = None
	member_status = None
	text = None
	time = None
class FaveTag:
	"""VK Object FaveTag

	id - Tag id
	name - Tag name
	"""
	id = None
	name = None
class FriendsFriendsList:
	"""VK Object FriendsFriendsList

	id - List ID
	name - List title
	"""
	id = None
	name = None
class GiftsLayout:
	"""VK Object GiftsLayout

	id - Gift ID
	thumb_512 - URL of the preview image with 512 px in width
	thumb_256 - URL of the preview image with 256 px in width
	thumb_48 - URL of the preview image with 48 px in width
	thumb_96 - URL of the preview image with 96 px in width
	stickers_product_id - ID of the sticker pack, if the gift is representing one
	is_stickers_style - Information whether gift represents a stickers style
	build_id - ID of the build of constructor gift
	keywords - Keywords used for search
	"""
	id = None
	thumb_512 = None
	thumb_256 = None
	thumb_48 = None
	thumb_96 = None
	stickers_product_id = None
	is_stickers_style = None
	build_id = None
	keywords = None
class GroupsAddress:
	"""VK Object GroupsAddress

	additional_address - Additional address to the place (6 floor, left door)
	address - String address to the place (Nevsky, 28)
	city_id - City id of address
	country_id - Country id of address
	distance - Distance from the point
	id - Address id
	latitude - Address latitude
	longitude - Address longitude
	metro_station_id - Metro id of address
	phone - Address phone
	time_offset - Time offset int minutes from utc time
	timetable - Week timetable for the address
	title - Title of the place (Zinger, etc)
	work_info_status - Status of information about timetable
	"""
	additional_address = None
	address = None
	city_id = None
	country_id = None
	distance = None
	id = None
	latitude = None
	longitude = None
	metro_station_id = None
	phone = None
	time_offset = None
	timetable = None
	title = None
	work_info_status = None
class GroupsAddressTimetable:
	"""VK Object GroupsAddressTimetable

	fri - Timetable for friday
	mon - Timetable for monday
	sat - Timetable for saturday
	sun - Timetable for sunday
	thu - Timetable for thursday
	tue - Timetable for tuesday
	wed - Timetable for wednesday
	"""
	fri = None
	mon = None
	sat = None
	sun = None
	thu = None
	tue = None
	wed = None
class GroupsAddressTimetableDay:
	"""VK Object GroupsAddressTimetableDay

	break_close_time - Close time of the break in minutes
	break_open_time - Start time of the break in minutes
	close_time - Close time in minutes
	open_time - Open time in minutes
	"""
	break_close_time = None
	break_open_time = None
	close_time = None
	open_time = None
class GroupsAddressesInfo:
	"""VK Object GroupsAddressesInfo

	is_enabled - Information whether addresses is enabled
	main_address_id - Main address id for group
	"""
	is_enabled = None
	main_address_id = None
class GroupsContactsItem:
	"""VK Object GroupsContactsItem

	user_id - User ID
	desc - Contact description
	phone - Contact phone
	email - Contact email
	"""
	user_id = None
	desc = None
	phone = None
	email = None
class GroupsCountersGroup:
	"""VK Object GroupsCountersGroup

	addresses - Addresses number
	albums - Photo albums number
	audios - Audios number
	audio_playlists - Audio playlists number
	docs - Docs number
	market - Market items number
	photos - Photos number
	topics - Topics number
	videos - Videos number
	"""
	addresses = None
	albums = None
	audios = None
	audio_playlists = None
	docs = None
	market = None
	photos = None
	topics = None
	videos = None
class GroupsGroupAttach:
	"""VK Object GroupsGroupAttach

	id - group ID
	text - text of attach
	status - activity or category of group
	size - size of group
	is_favorite - is favorite
	"""
	id = None
	text = None
	status = None
	size = None
	is_favorite = None
class GroupsGroupLink:
	"""VK Object GroupsGroupLink

	name - Link label
	desc - Link description
	edit_title - Information whether the title can be edited
	id - Link ID
	image_processing - Information whether the image on processing
	url - Link URL
	"""
	name = None
	desc = None
	edit_title = None
	id = None
	image_processing = None
	url = None
class GroupsLinksItem:
	"""VK Object GroupsLinksItem

	desc - Link description
	edit_title - Information whether the link title can be edited
	id - Link ID
	name - Link title
	photo_100 - URL of square image of the link with 100 pixels in width
	photo_50 - URL of square image of the link with 50 pixels in width
	url - Link URL
	"""
	desc = None
	edit_title = None
	id = None
	name = None
	photo_100 = None
	photo_50 = None
	url = None
class GroupsLonGPollServer:
	"""VK Object GroupsLonGPollServer

	key - Long Poll key
	server - Long Poll server address
	ts - Number of the last event
	"""
	key = None
	server = None
	ts = None
class GroupsMemberStatus:
	"""VK Object GroupsMemberStatus

	member - Information whether user is a member of the group
	user_id - User ID
	"""
	member = None
	user_id = None
class GroupsMemberStatusFull:
	"""VK Object GroupsMemberStatusFull

	can_invite - Information whether user can be invited
	can_recall - Information whether user's invite to the group can be recalled
	invitation - Information whether user has been invited to the group
	member - Information whether user is a member of the group
	request - Information whether user has send request to the group
	user_id - User ID
	"""
	can_invite = None
	can_recall = None
	invitation = None
	member = None
	request = None
	user_id = None
class GroupsProfileItem:
	"""VK Object GroupsProfileItem

	id - User id
	photo_50 - Url for user photo
	photo_100 - Url for user photo
	first_name - User first name
	"""
	id = None
	photo_50 = None
	photo_100 = None
	first_name = None
class GroupsSubjectItem:
	"""VK Object GroupsSubjectItem

	id - Subject ID
	name - Subject title
	"""
	id = None
	name = None
class LinkTargetObject:
	"""VK Object LinkTargetObject

	type - Object type
	owner_id - Owner ID
	item_id - Item ID
	"""
	type = None
	owner_id = None
	item_id = None
class MarketCurrency:
	"""VK Object MarketCurrency

	id - Currency ID
	name - Currency sign
	"""
	id = None
	name = None
class MarketSection:
	"""VK Object MarketSection

	id - Section ID
	name - Section name
	"""
	id = None
	name = None
class MessagesChatPushSettings:
	"""VK Object MessagesChatPushSettings

	disabled_until - Time until that notifications are disabled
	sound - Information whether the sound is on
	"""
	disabled_until = None
	sound = None
class MessagesChatRestrictions:
	"""VK Object MessagesChatRestrictions

	admins_promote_users - Only admins can promote users to admins
	only_admins_edit_info - Only admins can change chat info
	only_admins_edit_pin - Only admins can edit pinned message
	only_admins_invite - Only admins can invite users to this chat
	only_admins_kick - Only admins can kick users from this chat
	"""
	admins_promote_users = None
	only_admins_edit_info = None
	only_admins_edit_pin = None
	only_admins_invite = None
	only_admins_kick = None
class MessagesChatSettingsAcl:
	"""VK Object MessagesChatSettingsAcl

	can_change_info - Can you change photo, description and name
	can_change_invite_link - Can you change invite link for this chat
	can_change_pin - Can you pin/unpin message for this chat
	can_invite - Can you invite other peers in chat
	can_promote_users - Can you promote simple users to chat admins
	can_see_invite_link - Can you see invite link for this chat
	can_moderate - Can you moderate (delete) other users' messages
	can_copy_chat - Can you copy chat
	can_call - Can you init group call in the chat
	can_use_mass_mentions - Can you use mass mentions
	can_change_service_type - Can you change chat service type
	"""
	can_change_info = None
	can_change_invite_link = None
	can_change_pin = None
	can_invite = None
	can_promote_users = None
	can_see_invite_link = None
	can_moderate = None
	can_copy_chat = None
	can_call = None
	can_use_mass_mentions = None
	can_change_service_type = None
class MessagesChatSettingsPerMissions:
	"""VK Object MessagesChatSettingsPerMissions

	invite - Who can invite users to chat
	change_info - Who can change chat info
	change_pin - Who can change pinned message
	use_mass_mentions - Who can use mass mentions
	see_invite_link - Who can see invite link
	call - Who can make calls
	change_admins - Who can change admins
	"""
	invite = None
	change_info = None
	change_pin = None
	use_mass_mentions = None
	see_invite_link = None
	call = None
	change_admins = None
class MessagesChatSettingsPhoto:
	"""VK Object MessagesChatSettingsPhoto

	photo_50 - URL of the preview image with 50px in width
	photo_100 - URL of the preview image with 100px in width
	photo_200 - URL of the preview image with 200px in width
	is_default_photo - If provided photo is default
	"""
	photo_50 = None
	photo_100 = None
	photo_200 = None
	is_default_photo = None
class MessagesConversationSortId:
	"""VK Object MessagesConversationSortId

	major_id - Major id for sorting conversations
	minor_id - Minor id for sorting conversations
	"""
	major_id = None
	minor_id = None
class MessagesGraffiti:
	"""VK Object MessagesGraffiti

	access_key - Access key for graffiti
	height - Graffiti height
	id - Graffiti ID
	owner_id - Graffiti owner ID
	url - Graffiti URL
	width - Graffiti width
	"""
	access_key = None
	height = None
	id = None
	owner_id = None
	url = None
	width = None
class MessagesKeyboardButtonAction:
	"""VK Object MessagesKeyboardButtonAction

	app_id - Fragment value in app link like vk.com/app{app_id}_-654321#hash
	hash - Fragment value in app link like vk.com/app123456_-654321#{hash}
	label - Label for button
	link - link for button
	owner_id - Fragment value in app link like vk.com/app123456_{owner_id}#hash
	payload - Additional data sent along with message for developer convenience
	type - Button type
	"""
	app_id = None
	hash = None
	label = None
	link = None
	owner_id = None
	payload = None
	type = None
class MessagesLastActivity:
	"""VK Object MessagesLastActivity

	online - Information whether user is online
	time - Time when user was online in Unixtime
	"""
	online = None
	time = None
class MessagesLongpollParaMs:
	"""VK Object MessagesLongpollParaMs

	server - Server URL
	key - Key
	ts - Timestamp
	pts - Persistent timestamp
	"""
	server = None
	key = None
	ts = None
	pts = None
class MessagesMessageActionPhoto:
	"""VK Object MessagesMessageActionPhoto

	photo_100 - URL of the preview image with 100px in width
	photo_200 - URL of the preview image with 200px in width
	photo_50 - URL of the preview image with 50px in width
	"""
	photo_100 = None
	photo_200 = None
	photo_50 = None
class MessagesMessageRequestData:
	"""VK Object MessagesMessageRequestData

	status - Status of message request
	inviter_id - Message request sender id
	request_date - Message request date
	"""
	status = None
	inviter_id = None
	request_date = None
class MessagesPushSettings:
	"""VK Object MessagesPushSettings

	disabled_forever - Information whether push notifications are disabled forever
	disabled_until - Time until what notifications are disabled
	no_sound - Information whether the sound is on
	"""
	disabled_forever = None
	disabled_until = None
	no_sound = None
class NewsfeedEveNtActivity:
	"""VK Object NewsfeedEveNtActivity

	address - address of event
	button_text - text of attach
	friends - array of friends ids
	member_status - Current user's member status
	text - text of attach
	time - event start time
	"""
	address = None
	button_text = None
	friends = None
	member_status = None
	text = None
	time = None
class NewsfeedList:
	"""VK Object NewsfeedList

	id - List ID
	title - List title
	"""
	id = None
	title = None
class NotesNoteCommeNt:
	"""VK Object NotesNoteCommeNt

	date - Date when the comment has beed added in Unixtime
	id - Comment ID
	message - Comment text
	nid - Note ID
	oid - Note ID
	reply_to - ID of replied comment 
	uid - Comment author's ID
	"""
	date = None
	id = None
	message = None
	nid = None
	oid = None
	reply_to = None
	uid = None
class NotificatioNsReply:
	"""VK Object NotificatioNsReply

	date - Date when the reply has been created in Unixtime
	id - Reply ID
	text - Reply text
	"""
	date = None
	id = None
	text = None
class NotificatioNsSeNdMessageError:
	"""VK Object NotificatioNsSeNdMessageError

	code - Error code
	description - Error description
	"""
	code = None
	description = None
class OauthErrOr:
	"""VK Object OauthErrOr

	error - Error type
	error_description - Error description
	redirect_uri - URI for validation
	"""
	error = None
	error_description = None
	redirect_uri = None
class OrdersAmOuntItem:
	"""VK Object OrdersAmOuntItem

	amount - Votes amount in user's currency
	description - Amount description
	votes - Votes number
	"""
	amount = None
	description = None
	votes = None
class OrdersOrder:
	"""VK Object OrdersOrder

	amount - Amount
	app_order_id - App order ID
	cancel_transaction_id - Cancel transaction ID
	date - Date of creation in Unixtime
	id - Order ID
	item - Order item
	receiver_id - Receiver ID
	status - Order status
	transaction_id - Transaction ID
	user_id - User ID
	"""
	amount = None
	app_order_id = None
	cancel_transaction_id = None
	date = None
	id = None
	item = None
	receiver_id = None
	status = None
	transaction_id = None
	user_id = None
class OrdersSubscriptiOn:
	"""VK Object OrdersSubscriptiOn

	cancel_reason - Cancel reason
	create_time - Date of creation in Unixtime
	id - Subscription ID
	item_id - Subscription order item
	next_bill_time - Date of next bill in Unixtime
	pending_cancel - Pending cancel state
	period - Subscription period
	period_start_time - Date of last period start in Unixtime
	price - Subscription price
	status - Subscription status
	test_mode - Is test subscription
	trial_expire_time - Date of trial expire in Unixtime
	update_time - Date of last change in Unixtime
	"""
	cancel_reason = None
	create_time = None
	id = None
	item_id = None
	next_bill_time = None
	pending_cancel = None
	period = None
	period_start_time = None
	price = None
	status = None
	test_mode = None
	trial_expire_time = None
	update_time = None
class PagesWikiPage:
	"""VK Object PagesWikiPage

	creator_id - Page creator ID
	creator_name - Page creator name
	editor_id - Last editor ID
	editor_name - Last editor name
	group_id - Community ID
	id - Page ID
	title - Page title
	views - Views number
	who_can_edit - Edit settings of the page
	who_can_view - View settings of the page
	"""
	creator_id = None
	creator_name = None
	editor_id = None
	editor_name = None
	group_id = None
	id = None
	title = None
	views = None
	who_can_edit = None
	who_can_view = None
class PagesWikiPageFull:
	"""VK Object PagesWikiPageFull

	created - Date when the page has been created in Unixtime
	creator_id - Page creator ID
	current_user_can_edit - Information whether current user can edit the page
	current_user_can_edit_access - Information whether current user can edit the page access settings
	edited - Date when the page has been edited in Unixtime
	editor_id - Last editor ID
	group_id - Community ID
	html - Page content, HTML
	id - Page ID
	source - Page content, wiki
	title - Page title
	view_url - URL of the page preview
	views - Views number
	who_can_edit - Edit settings of the page
	who_can_view - View settings of the page
	"""
	created = None
	creator_id = None
	current_user_can_edit = None
	current_user_can_edit_access = None
	edited = None
	editor_id = None
	group_id = None
	html = None
	id = None
	source = None
	title = None
	view_url = None
	views = None
	who_can_edit = None
	who_can_view = None
class PagesWikiPageHistory:
	"""VK Object PagesWikiPageHistory

	id - Version ID
	length - Page size in bytes
	date - Date when the page has been edited in Unixtime
	editor_id - Last editor ID
	editor_name - Last editor name
	"""
	id = None
	length = None
	date = None
	editor_id = None
	editor_name = None
class PhotosPhotoTag:
	"""VK Object PhotosPhotoTag

	date - Date when tag has been added in Unixtime
	id - Tag ID
	placer_id - ID of the tag creator
	tagged_name - Tag description
	description - Tagged description.
	user_id - Tagged user ID
	viewed - Information whether the tag is reviewed
	x - Coordinate X of the left upper corner
	x2 - Coordinate X of the right lower corner
	y - Coordinate Y of the left upper corner
	y2 - Coordinate Y of the right lower corner
	"""
	date = None
	id = None
	placer_id = None
	tagged_name = None
	description = None
	user_id = None
	viewed = None
	x = None
	x2 = None
	y = None
	y2 = None
class PhotosPhotoUPload:
	"""VK Object PhotosPhotoUPload

	album_id - Album ID
	upload_url - URL to upload photo
	fallback_upload_url - Fallback URL if upload_url returned error
	user_id - User ID
	group_id - Group ID
	"""
	album_id = None
	upload_url = None
	fallback_upload_url = None
	user_id = None
	group_id = None
class PodcastExternalData:
	"""VK Object PodcastExternalData

	url - Url of the podcast page
	owner_url - Url of the podcasts owner community
	title - Podcast title
	owner_name - Name of the podcasts owner community
	cover - Podcast cover
	"""
	url = None
	owner_url = None
	title = None
	owner_name = None
	cover = None
class PollsAnswer:
	"""VK Object PollsAnswer

	id - Answer ID
	rate - Answer rate in percents
	text - Answer text
	votes - Votes number
	"""
	id = None
	rate = None
	text = None
	votes = None
class SecureLevel:
	"""VK Object SecureLevel

	level - Level
	uid - User ID
	"""
	level = None
	uid = None
class SecureSmSNotification:
	"""VK Object SecureSmSNotification

	app_id - Application ID
	date - Date when message has been sent in Unixtime
	id - Notification ID
	message - Messsage text
	user_id - User ID
	"""
	app_id = None
	date = None
	id = None
	message = None
	user_id = None
class SecureTokenChecked:
	"""VK Object SecureTokenChecked

	date - Date when access_token has been generated in Unixtime
	expire - Date when access_token will expire in Unixtime
	success - Returns if successfully processed
	user_id - User ID
	"""
	date = None
	expire = None
	success = None
	user_id = None
class SecureTranSaction:
	"""VK Object SecureTranSaction

	date - Transaction date in Unixtime
	id - Transaction ID
	uid_from - From ID
	uid_to - To ID
	votes - Votes number
	"""
	date = None
	id = None
	uid_from = None
	uid_to = None
	votes = None
class StatSActivity:
	"""VK Object StatSActivity

	comments - Comments number
	copies - Reposts number
	hidden - Hidden from news count
	likes - Likes number
	subscribed - New subscribers count
	unsubscribed - Unsubscribed count
	"""
	comments = None
	copies = None
	hidden = None
	likes = None
	subscribed = None
	unsubscribed = None
class StatSCity:
	"""VK Object StatSCity

	count - Visitors number
	name - City name
	value - City ID
	"""
	count = None
	name = None
	value = None
class StatSCountry:
	"""VK Object StatSCountry

	code - Country code
	count - Visitors number
	name - Country name
	value - Country ID
	"""
	code = None
	count = None
	name = None
	value = None
class StickerSImageSet:
	"""VK Object StickerSImageSet

	base_url - Base URL for images in set
	version - Version number to be appended to the image URL
	"""
	base_url = None
	version = None
class StoreStickerSKeywordSticker:
	"""VK Object StoreStickerSKeywordSticker

	pack_id - Pack id
	sticker_id - Sticker id
	"""
	pack_id = None
	sticker_id = None
class StorieSPromoBlock:
	"""VK Object StorieSPromoBlock

	name - Promo story title
	photo_50 - RL of square photo of the story with 50 pixels in width
	photo_100 - RL of square photo of the story with 100 pixels in width
	not_animated - Hide animation for promo story
	"""
	name = None
	photo_50 = None
	photo_100 = None
	not_animated = None
class StorieSReplieS:
	"""VK Object StorieSReplieS

	count - Replies number.
	new - New replies number.
	"""
	count = None
	new = None
class StorieSStoryLink:
	"""VK Object StorieSStoryLink

	text - Link text
	url - Link URL
	"""
	text = None
	url = None
class UsersCareer:
	"""VK Object UsersCareer

	city_id - City ID
	city_name - City name
	company - Company name
	country_id - Country ID
	from - From year
	group_id - Community ID
	id - Career ID
	position - Position
	until - Till year
	"""
	city_id = None
	city_name = None
	company = None
	country_id = None
	_from = None
	group_id = None
	id = None
	position = None
	until = None
class UsersLastSeen:
	"""VK Object UsersLastSeen

	platform - Type of the platform that used for the last authorization
	time - Last visit date (in Unix time)
	"""
	platform = None
	time = None
class UsersMilitary:
	"""VK Object UsersMilitary

	country_id - Country ID
	from - From year
	id - Military ID
	unit - Unit name
	unit_id - Unit ID
	until - Till year
	"""
	country_id = None
	_from = None
	id = None
	unit = None
	unit_id = None
	until = None
class UsersOccUpation:
	"""VK Object UsersOccUpation

	id - ID of school, university, company group
	name - Name of occupation
	type - Type of occupation
	"""
	id = None
	name = None
	type = None
class UsersOnlineInfo:
	"""VK Object UsersOnlineInfo

	visible - Whether you can see real online status of user or not
	last_seen - Last time we saw user being active
	is_online - Whether user is currently online or not
	app_id - Application id from which user is currently online or was last seen online
	is_mobile - Is user online from desktop app or mobile app
	status - In case user online is not visible, it indicates approximate timeframe of user online
	"""
	visible = None
	last_seen = None
	is_online = None
	app_id = None
	is_mobile = None
	status = None
class UsersRelative:
	"""VK Object UsersRelative

	birth_date - Date of child birthday (format dd.mm.yyyy)
	id - Relative ID
	name - Name of relative
	type - Relative type
	"""
	birth_date = None
	id = None
	name = None
	type = None
class UsersUserConnections:
	"""VK Object UsersUserConnections

	skype - User's Skype nickname
	facebook - User's Facebook account
	facebook_name - User's Facebook name
	twitter - User's Twitter account
	livejournal - User's Livejournal account
	instagram - User's Instagram account
	"""
	skype = None
	facebook = None
	facebook_name = None
	twitter = None
	livejournal = None
	instagram = None
class UtilsLastShortenedLink:
	"""VK Object UtilsLastShortenedLink

	access_key - Access key for private stats
	key - Link key (characters after vk.cc/)
	short_url - Short link URL
	timestamp - Creation time in Unixtime
	url - Full URL
	views - Total views number
	"""
	access_key = None
	key = None
	short_url = None
	timestamp = None
	url = None
	views = None
class UtilsShortLink:
	"""VK Object UtilsShortLink

	access_key - Access key for private stats
	key - Link key (characters after vk.cc/)
	short_url - Short link URL
	url - Full URL
	"""
	access_key = None
	key = None
	short_url = None
	url = None
class UtilsStats:
	"""VK Object UtilsStats

	timestamp - Start time
	views - Total views number
	"""
	timestamp = None
	views = None
class UtilsStatsCity:
	"""VK Object UtilsStatsCity

	city_id - City ID
	views - Views number
	"""
	city_id = None
	views = None
class UtilsStatsCoUntry:
	"""VK Object UtilsStatsCoUntry

	country_id - Country ID
	views - Views number
	"""
	country_id = None
	views = None
class UtilsStatsSexAge:
	"""VK Object UtilsStatsSexAge

	age_range - Age denotation
	female -  Views by female users
	male -  Views by male users
	"""
	age_range = None
	female = None
	male = None
class VideoLiVeSettings:
	"""VK Object VideoLiVeSettings

	can_rewind - If user car rewind live or not
	is_endless - If live is endless or not
	max_duration - Max possible time for rewind
	"""
	can_rewind = None
	is_endless = None
	max_duration = None
class VideoSaVeResult:
	"""VK Object VideoSaVeResult

	access_key - Video access key
	description - Video description
	owner_id - Video owner ID
	title - Video title
	upload_url - URL for the video uploading
	video_id - Video ID
	"""
	access_key = None
	description = None
	owner_id = None
	title = None
	upload_url = None
	video_id = None
class VideoVideoAlbumFull:
	"""VK Object VideoVideoAlbumFull

	count - Total number of videos in album
	id - Album ID
	image - Album cover image in different sizes
	image_blur - Need blur album thumb or not
	is_system - Information whether album is system
	owner_id - Album owner's ID
	title - Album title
	updated_time - Date when the album has been updated last time in Unixtime
	"""
	count = None
	id = None
	image = None
	image_blur = None
	is_system = None
	owner_id = None
	title = None
	updated_time = None
class VideoVideoFiles:
	"""VK Object VideoVideoFiles

	external - URL of the external player
	mp4_240 - URL of the mpeg4 file with 240p quality
	mp4_360 - URL of the mpeg4 file with 360p quality
	mp4_480 - URL of the mpeg4 file with 480p quality
	mp4_720 - URL of the mpeg4 file with 720p quality
	mp4_1080 - URL of the mpeg4 file with 1080p quality
	flv_320 - URL of the flv file with 320p quality
	"""
	external = None
	mp4_240 = None
	mp4_360 = None
	mp4_480 = None
	mp4_720 = None
	mp4_1080 = None
	flv_320 = None
class WallAppPost:
	"""VK Object WallAppPost

	id - Application ID
	name - Application name
	photo_130 - URL of the preview image with 130 px in width
	photo_604 - URL of the preview image with 604 px in width
	"""
	id = None
	name = None
	photo_130 = None
	photo_604 = None
class WallAttachedNote:
	"""VK Object WallAttachedNote

	comments - Comments number
	date - Date when the note has been created in Unixtime
	id - Note ID
	owner_id - Note owner's ID
	read_comments - Read comments number
	title - Note title
	view_url - URL of the page with note preview
	"""
	comments = None
	date = None
	id = None
	owner_id = None
	read_comments = None
	title = None
	view_url = None
class WallCarouselBase:
	"""VK Object WallCarouselBase

	carousel_offset - Index of current carousel element
	"""
	carousel_offset = None
class WallGraffiti:
	"""VK Object WallGraffiti

	id - Graffiti ID
	owner_id - Graffiti owner's ID
	photo_200 - URL of the preview image with 200 px in width
	photo_586 - URL of the preview image with 586 px in width
	"""
	id = None
	owner_id = None
	photo_200 = None
	photo_586 = None
class WallPostedPhoto:
	"""VK Object WallPostedPhoto

	id - Photo ID
	owner_id - Photo owner's ID
	photo_130 - URL of the preview image with 130 px in width
	photo_604 - URL of the preview image with 604 px in width
	"""
	id = None
	owner_id = None
	photo_130 = None
	photo_604 = None
class WallVieWs:
	"""VK Object WallVieWs

	count - Count
	"""
	count = None
class WallWallpostDonut:
	"""VK Object WallWallpostDonut

	is_donut - Post only for dons
	paid_duration - Value of this field need to pass in wall.post/edit in donut_paid_duration
	placeholder - If placeholder was respond, text and all attachments will be hidden
	can_publish_free_copy - Says whether group admin can post free copy of this donut post
	edit_mode - Says what user can edit in post about donut properties
	"""
	is_donut = None
	paid_duration = None
	placeholder = None
	can_publish_free_copy = None
	edit_mode = None
class WidgetsWidgetLikes:
	"""VK Object WidgetsWidgetLikes

	count - Likes number
	"""
	count = None
