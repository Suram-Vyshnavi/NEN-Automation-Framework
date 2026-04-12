from locators.rm_locators import cohorts_locators as rm_cohorts_locators
from utils.helpers import attach_screenshot, highlight_element


class RMCohortsPage:
    def __init__(self, page):
        self.page = page

    def click_on_cohorts_tab(self):
        try:
            cohorts_tab = self.page.locator(rm_cohorts_locators.COHORTS_HEADER)
            cohorts_tab.wait_for(state="visible", timeout=15000)
            cohorts_tab.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Click Cohorts Tab Failed")
            print(f"RM click cohorts tab failed: {e}")

    def validate_direct_cohorts_heading(self):
        try:
            heading = self.page.locator(rm_cohorts_locators.DIRECT_COHORTS_HEADING)
            heading.wait_for(state="visible", timeout=15000)
            assert heading.is_visible(), "Direct Cohorts heading is not visible"
            highlight_element(self.page, rm_cohorts_locators.DIRECT_COHORTS_HEADING)
        except Exception as e:
            attach_screenshot(self.page, "RM Direct Cohorts Heading Validation Failed")
            print(f"RM direct cohorts heading validation failed: {e}")

    def validate_status_heading(self):
        try:
            status = self.page.locator(rm_cohorts_locators.STATUS)
            status.wait_for(state="visible", timeout=15000)
            assert status.is_visible(), "Status heading is not visible"
            highlight_element(self.page, rm_cohorts_locators.STATUS)
        except Exception as e:
            attach_screenshot(self.page, "RM Status Heading Validation Failed")
            print(f"RM status heading validation failed: {e}")

    def click_on_active_tab(self):
        try:
            active_tab = self.page.locator(rm_cohorts_locators.ACTIVE_TAB)
            active_tab.wait_for(state="visible", timeout=15000)
            active_tab.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Click Active Tab Failed")
            print(f"RM click active tab failed: {e}")

    def click_on_first_active_cohort(self):
        try:
            cohort = self.page.locator(rm_cohorts_locators.SELECT_COHORT)
            cohort.wait_for(state="visible", timeout=15000)
            cohort.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Click First Active Cohort Failed")
            print(f"RM click first active cohort failed: {e}")

    def validate_all_tabs_in_cohort_page(self):
        try:
            tabs = [
                rm_cohorts_locators.COHORT_DASHBOARD_TAB,
                rm_cohorts_locators.SCORE_CARD_TAB,
                rm_cohorts_locators.GENERAL_INFO_TAB,
                rm_cohorts_locators.RELEASE_MILESTONE_TAB,
                rm_cohorts_locators.COHORT_VENTURES_TAB,
                rm_cohorts_locators.COHORT_MEMBERS_TAB,
            ]

            for tab_locator in tabs:
                tab = self.page.locator(tab_locator)
                tab.first.wait_for(state="visible", timeout=15000)
                assert tab.first.is_visible(), f"Tab not visible: {tab_locator}"
                tab.first.click()
                highlight_element(self.page, tab_locator)

            self.page.go_back()
        except Exception as e:
            attach_screenshot(self.page, "RM Validate All Direct Cohort Tabs Failed")
            print(f"RM validate all direct cohort tabs failed: {e}")

    def validate_pagination(self):
        try:
            page_2 = self.page.locator(rm_cohorts_locators.PAGE_NUMBER)
            page_2.wait_for(state="visible", timeout=15000)
            assert page_2.is_visible(), "Pagination page 2 is not visible"
            highlight_element(self.page, rm_cohorts_locators.PAGE_NUMBER)
            page_2.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Direct Cohorts Pagination Validation Failed")
            print(f"RM direct cohorts pagination validation failed: {e}")

    def click_on_inactive_tab(self):
        try:
            inactive_tab = self.page.locator(rm_cohorts_locators.INACTIVE_TAB)
            inactive_tab.wait_for(state="visible", timeout=15000)
            inactive_tab.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Click Inactive Tab Failed")
            print(f"RM click inactive tab failed: {e}")

    def search_for_test_cohort(self):
        try:
            search = self.page.locator(rm_cohorts_locators.SEARCH_COHORT_INPUT)
            search.wait_for(state="visible", timeout=15000)
            search.fill("test")
        except Exception as e:
            attach_screenshot(self.page, "RM Search Test Cohort Failed")
            print(f"RM search test cohort failed: {e}")

    def validate_incubator_cohorts_heading(self):
        try:
            heading = self.page.locator(rm_cohorts_locators.INCUBATOR_COHORTS_HEADING)
            heading.wait_for(state="visible", timeout=15000)
            assert heading.is_visible(), "Incubator Cohorts heading is not visible"
            highlight_element(self.page, rm_cohorts_locators.INCUBATOR_COHORTS_HEADING)
        except Exception as e:
            attach_screenshot(self.page, "RM Incubator Cohorts Heading Validation Failed")
            print(f"RM incubator cohorts heading validation failed: {e}")

    def validate_incubator_status_heading(self):
        try:
            status = self.page.locator(rm_cohorts_locators.INCUBATOR_STATUS)
            status.wait_for(state="visible", timeout=15000)
            assert status.is_visible(), "Incubator status heading is not visible"
            highlight_element(self.page, rm_cohorts_locators.INCUBATOR_STATUS)
        except Exception as e:
            attach_screenshot(self.page, "RM Incubator Status Heading Validation Failed")
            print(f"RM incubator status heading validation failed: {e}")

    def click_on_incubator_active_tab(self):
        try:
            active_tab = self.page.locator(rm_cohorts_locators.INCUBATOR_ACTIVE_TAB)
            active_tab.wait_for(state="visible", timeout=15000)
            active_tab.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Click Incubator Active Tab Failed")
            print(f"RM click incubator active tab failed: {e}")

    def click_on_incubator_first_active_cohort(self):
        try:
            cohort = self.page.locator(rm_cohorts_locators.INCUBATOR_FIRST_ROW_LAST_COLUMN)
            cohort.wait_for(state="visible", timeout=15000)
            cohort.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Click Incubator First Active Cohort Failed")
            print(f"RM click incubator first active cohort failed: {e}")

    def validate_incubator_all_tabs_in_cohort_page(self):
        try:
            tabs = [
                rm_cohorts_locators.COHORT_DASHBOARD_TAB,
                rm_cohorts_locators.GENERAL_INFO_TAB,
                rm_cohorts_locators.COHORT_MEMBERS_TAB,
                rm_cohorts_locators.COHORT_STARTUPS_TAB,
            ]

            for tab_locator in tabs:
                tab = self.page.locator(tab_locator)
                tab.first.wait_for(state="visible", timeout=15000)
                assert tab.first.is_visible(), f"Incubator tab not visible: {tab_locator}"
                tab.first.click()
                highlight_element(self.page, tab_locator)

            self.page.go_back()
        except Exception as e:
            attach_screenshot(self.page, "RM Validate All Incubator Cohort Tabs Failed")
            print(f"RM validate all incubator cohort tabs failed: {e}")

    def validate_incubator_pagination(self):
        try:
            page_2 = self.page.locator(rm_cohorts_locators.PAGE_NUMBER)
            page_2.wait_for(state="visible", timeout=15000)
            assert page_2.is_visible(), "Incubator pagination page 2 is not visible"
            highlight_element(self.page, rm_cohorts_locators.PAGE_NUMBER)
            page_2.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Incubator Cohorts Pagination Validation Failed")
            print(f"RM incubator cohorts pagination validation failed: {e}")

    def search_for_test_cohort_in_incubator(self):
        try:
            search = self.page.locator(rm_cohorts_locators.INCUBATOR_SEARCH_COHORT_INPUT)
            search.wait_for(state="visible", timeout=15000)
            search.fill("test")
        except Exception as e:
            attach_screenshot(self.page, "RM Search Test Cohort In Incubator Failed")
            print(f"RM search test cohort in incubator failed: {e}")
