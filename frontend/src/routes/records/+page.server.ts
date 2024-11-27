import { remove } from "../../services/core.service"
import { remove_patient } from "../../services/patient.service"
export const actions = {
    deletePatient: async({request})=>{
        let data = await request.formData()
        let id = data.get("id")
        console.log(id)
        await remove_patient(id)
        return {
            success: true,
            message: 'Yay!!'
        }
    }
}