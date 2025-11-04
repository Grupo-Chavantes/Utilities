class SipefInferencesController < ApplicationController
  before_action :set_sipef_inference, only: %i[ show edit update destroy ]

  # GET /sipef_inferences or /sipef_inferences.json
  def index
    @sipef_inferences = SipefInference.all
  end

  # GET /sipef_inferences/1 or /sipef_inferences/1.json
  def show
  end

  # GET /sipef_inferences/new
  def new
    @sipef_inference = SipefInference.new
  end

  # GET /sipef_inferences/1/edit
  def edit
  end

  # POST /sipef_inferences or /sipef_inferences.json
  def create
    @sipef_inference = SipefInference.new(sipef_inference_params)

    respond_to do |format|
      if @sipef_inference.save
        format.html { redirect_to @sipef_inference, notice: "Sipef inference was successfully created." }
        format.json { render :show, status: :created, location: @sipef_inference }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @sipef_inference.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /sipef_inferences/1 or /sipef_inferences/1.json
  def update
    respond_to do |format|
      if @sipef_inference.update(sipef_inference_params)
        format.html { redirect_to @sipef_inference, notice: "Sipef inference was successfully updated.", status: :see_other }
        format.json { render :show, status: :ok, location: @sipef_inference }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @sipef_inference.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /sipef_inferences/1 or /sipef_inferences/1.json
  def destroy
    @sipef_inference.destroy!

    respond_to do |format|
      format.html { redirect_to sipef_inferences_path, notice: "Sipef inference was successfully destroyed.", status: :see_other }
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
      params.expect(sipef_inference: [ :status ])
    end
end
