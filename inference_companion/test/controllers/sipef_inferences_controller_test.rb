require "test_helper"

class SipefInferencesControllerTest < ActionDispatch::IntegrationTest
  setup do
    @sipef_inference = sipef_inferences(:one)
  end

  test "should get index" do
    get sipef_inferences_url
    assert_response :success
  end

  test "should get new" do
    get new_sipef_inference_url
    assert_response :success
  end

  test "should create sipef_inference" do
    assert_difference("SipefInference.count") do
      post sipef_inferences_url, params: { sipef_inference: { status: @sipef_inference.status } }
    end

    assert_redirected_to sipef_inference_url(SipefInference.last)
  end

  test "should destroy sipef_inference" do
    assert_difference("SipefInference.count", -1) do
      delete sipef_inference_url(@sipef_inference)
    end

    assert_redirected_to sipef_inferences_url
  end
end
