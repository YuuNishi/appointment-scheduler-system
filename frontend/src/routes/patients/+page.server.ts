import { fail,redirect } from "@sveltejs/kit"

export const load = async()=> {
    const getPatients = async()=>{
        const resp = await fetch('http://127.0.0.1:8000/api/patient',{headers: {Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU0NzIzYjJmLTEyYTktNGVkNi1iYzVmLWU3M2Y5N2E0MTZhOSIsImVtYWlsIjoidW1pQGV4YW1wbGUuY29tIiwiZXhwIjoxNzMyNTA1MTYxfQ.tgMF5159pQUWBA0qmDnbu59-Qzglt8VmMNA0TT97OAc','Content-Type': 'application/json'}})
        const data =await resp.json()
        return data.reverse()
    }
    return {
        patients:await getPatients(),
    }
}

 
export const actions = {
    updatePatient: async ({ request }) => {
        const data = await request.formData();

        let patient ={
            name: data.get("name"),
            status: parseInt(data.get("status")),
            sex: parseInt(data.get("gender")),
            birth_date: data.get("birthdate").split("/").reverse().join("-"),
            cpf: data.get("cpf")
        }
        if (isNaN(new Date(data.get('birthdate').split("/").reverse().join("/")))){
            return fail(400,{message: 'Invalid date', invalid: true})
        }
        console.log(patient); 
        let id = data.get("id")
        async function editPatient(patient) {
            const response2 = fetch(`http://127.0.0.1:8000/api/patient/${id}`,{
            method: 'PUT',
            headers: {Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU0NzIzYjJmLTEyYTktNGVkNi1iYzVmLWU3M2Y5N2E0MTZhOSIsImVtYWlsIjoidW1pQGV4YW1wbGUuY29tIiwiZXhwIjoxNzMyNTA1MTYxfQ.tgMF5159pQUWBA0qmDnbu59-Qzglt8VmMNA0TT97OAc','Content-Type': 'application/json'},
            body: JSON.stringify(patient)
            })
        }
        await editPatient(patient)
        return {
            success: true,
            message: "Yayy!!"
        };
    },

    deletePatient: async({request})=>{
        const data = await request.formData();
        let id = parseInt(data.get("id"))
        await fetch(`http://127.0.0.1:8000/api/patient/${id}`,{method: 'DELETE', 
            headers: {Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU0NzIzYjJmLTEyYTktNGVkNi1iYzVmLWU3M2Y5N2E0MTZhOSIsImVtYWlsIjoidW1pQGV4YW1wbGUuY29tIiwiZXhwIjoxNzMyNTA1MTYxfQ.tgMF5159pQUWBA0qmDnbu59-Qzglt8VmMNA0TT97OAc','Content-Type': 'application/json'},})
        return{
            sucess: true,
            message: 'Yaaay!'
        }
    }
};