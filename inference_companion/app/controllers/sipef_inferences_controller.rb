class SipefInferencesController < ApplicationController
  before_action :set_sipef_inference, only: %i[ destroy ]

  # GET /sipef_inferences or /sipef_inferences.json
  def index
    @sipef_inferences = SipefInference.order(created_at: :desc).limit(15)
    @sipef_inference = SipefInference.new
  end

  # POST /sipef_inferences or /sipef_inferences.json
  def create
    @sipef_inference = SipefInference.new(sipef_inference_params)

    respond_to do |format|
      if @sipef_inference.save
        format.html { redirect_to sipef_inferences_path, notice: "Arquivo enviado para processamento." }
        format.json { render json: @sipef_inference, status: :created }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @sipef_inference.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /sipef_inferences/1 or /sipef_inferences/1.json
  def destroy
    @sipef_inference.destroy!

    respond_to do |format|
      format.html { redirect_to sipef_inferences_path, notice: "Arquivo excluído com sucesso.", status: :see_other }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_sipef_inference
      @sipef_inference = SipefInference.find(params.expect(:id))
    end

    # Only allow a list of trusted parameters through.
    def sipef_inference_params
      params.expect(sipef_inference: [ :input_file ])
    end
end
