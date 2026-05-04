from behave import then
from pages.common.digital_library_page import DigitalLibraryPage


@then("user clicks on digital library section")
def click_digital_library_section(context):
    if not hasattr(context, "digital_library_page"):
        context.digital_library_page = DigitalLibraryPage(context.page)
    context.digital_library_page.click_digital_library_section()


@then("user validates digital library page section")
def validate_digital_library_page_section(context):
    context.digital_library_page.validate_digital_library_page_section()


@then("user validates latest articles and videos section")
def validate_latest_articles_and_videos_section(context):
    context.digital_library_page.validate_latest_articles_and_videos_section()


@then("user validates what are you looking for section")
def validate_what_are_you_looking_for_section(context):
    context.digital_library_page.validate_what_are_you_looking_for_section()


@then("user validates experts videos section")
def validate_experts_videos_section(context):
    context.digital_library_page.validate_experts_videos_section()


@then("user validates casestudies section")
def validate_casestudies_section(context):
    context.digital_library_page.validate_casestudies_section()


@then("user validates caselets section")
def validate_caselets_section(context):
    context.digital_library_page.validate_caselets_section()


@then("user validates concept notes section")
def validate_concept_notes_section(context):
    context.digital_library_page.validate_concept_notes_section()


@then("user validates solution kits section")
def validate_solution_kits_section(context):
    context.digital_library_page.validate_solution_kits_section()


@then("user validates good reads section")
def validate_good_reads_section(context):
    context.digital_library_page.validate_good_reads_section()


@then("user searches test in search input")
def search_test_in_search_input(context):
    context.digital_library_page.search_test_in_search_input()


@then("user clicks on first search result")
def click_first_search_result(context):
    context.digital_library_page.click_first_search_result()


@then("user validates suggested article videos section and clicks back button")
def validate_suggested_article_videos_section_and_click_back_button(context):
    context.digital_library_page.validate_suggested_article_videos_section_and_click_back_button()
